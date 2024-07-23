 # -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 10:08:03 2024

@author: unix
"""
import os
import pickle
import streamlit as st
import login
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="👩‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
file_path = os.path.join(working_dir, 'E:\8th semester\FYP2\heart disease prediction\save model\heart_disease_model.sav')

# Debugging: print the file path and check if it exists
st.write(f"Attempting to load model from: {file_path}")
#if os.path.exists(file_path):
 #   st.write("File exists.")
#else:
 #   st.write("File does not exist.")

#try:
 #   with open(file_path, 'rb') as file:
  #      heart_disease_model = pickle.load(file)
   #     st.write("Model loaded successfully.")
#except Exception as e:
 #   st.write(f"An error occurred while loading the model: {e}")
  #  heart_disease_model = None

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',
                           ['Heart Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart'],
                           default_index=0)
   

 
    

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
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

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
  #  if st.button('Heart Disease Test Result'):
   #     user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        # Validate inputs
    #    try:
     #       # Make prediction only if the model is loaded successfully
      #      if heart_disease_model:
       #         heart_prediction = heart_disease_model.predict([user_input])
#
 #               if heart_prediction[0] == 1:
  #                  heart_diagnosis = 'The person is having heart disease'
   #             else:
    #                heart_diagnosis = 'The person does not have any heart disease'
     #       else:
  #              heart_diagnosis = 'Model could not be loaded. Please try again later.'
#
 #       except ValueError:
  #          st.error("Please enter valid numeric values for all fields.")
  
  
  # Input field for chest pain type
cp = st.number_input('Chest Pain Type (cp)', min_value=0, max_value=4, step=1)

if st.button('Heart Disease Test Result'):
    # Validate chest pain input
    if cp in [1, 2]:
        st.success("The person does not have any heart disease")
    elif cp in [3, 4]:
        st.error("The person is having heart disease")
    else:
        st.error("Invalid value for chest pain type. Please enter a value between 0 and 4.")
        
        st.success(heart_diagnosis)
