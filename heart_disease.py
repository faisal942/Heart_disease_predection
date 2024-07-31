import os
import pickle
import streamlit as st
import mysql.connector
from mysql.connector import Error
from streamlit_option_menu import option_menu

# Function to create a database connection
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Default XAMPP MySQL username
            password="",  # Default XAMPP MySQL password is empty
            database="mydatabase"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            st.write(f"Connected to MySQL database... MySQL Server version on {db_info}")
    except Error as e:
        st.error(f"Error: '{e}'")
    return connection

# Function to insert user data
def insert_user(connection, name, email, age):
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, age))
    connection.commit()
    user_id = cursor.lastrowid
    cursor.close()
    return user_id

# Function to insert heart disease prediction data
def insert_prediction(connection, user_id, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction_result):
    cursor = connection.cursor()
    query = """
    INSERT INTO heart_disease_predictions (
        user_id, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction_result
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, prediction_result))
    connection.commit()
    cursor.close()

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="👩‍⚕️")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Menu', ['Login', 'Heart Disease Prediction'], menu_icon='menu', default_index=0)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None

# Login Page
if selected == 'Login':
    st.title("User Login")
    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120)

    if st.button("Login"):
        connection = create_connection()
        if connection is not None:
            user_id = insert_user(connection, name, email, age)
            st.success("Logged in successfully!")
            st.session_state.logged_in = True
            st.session_state.user_id = user_id
            connection.close()

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    if not st.session_state.logged_in:
        st.warning("Please login first")
    else:
        st.title('Heart Disease Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input('Age', min_value=1, max_value=120, step=1)

        with col2:
            sex = st.selectbox('Sex', options=[0, 1])

        with col3:
            cp = st.number_input('Chest Pain types', min_value=0, max_value=4, step=1)

        with col1:
            trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200, step=1)

        with col2:
            chol = st.number_input('Serum Cholestoral in mg/dl', min_value=100, max_value=600, step=1)

        with col3:
            fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])

        with col1:
            restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, step=1)

        with col2:
            thalach = st.number_input('Maximum Heart Rate achieved', min_value=60, max_value=220, step=1)

        with col3:
            exang = st.selectbox('Exercise Induced Angina', options=[0, 1])

        with col1:
            oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0, max_value=10.0, step=0.1)

        with col2:
            slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, step=1)

        with col3:
            ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=4, step=1)

        with col1:
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2, step=1)

        if st.button('Heart Disease Test Result'):
            # Model prediction logic here
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

            # Dummy prediction logic (replace with actual model prediction)
            if cp in [1, 2]:
                heart_diagnosis = "The person does not have any heart disease"
            elif cp in [3, 4]:
                heart_diagnosis = "The person is having heart disease"
            else:
                heart_diagnosis = "Invalid value for chest pain type. Please enter a value between 0 and 4."

            st.success(heart_diagnosis)

            # Save prediction to database
            connection = create_connection()
            if connection is not None:
                insert_prediction(connection, st.session_state.user_id, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, heart_diagnosis)
                connection.close()
