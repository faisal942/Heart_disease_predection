import streamlit as st
import mysql.connector
from mysql.connector import Error

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

def insert_user(connection, name, email, age):
    cursor = connection.cursor()
    query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, age))
    connection.commit()
    cursor.close()

# Streamlit App
def main():
    st.title("Streamlit MySQL Database Integration with XAMPP")

    name = st.text_input("Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, max_value=120)

    if st.button("Submit"):
        connection = create_connection()
        if connection is not None:
            insert_user(connection, name, email, age)
            st.success("User added successfully!")
            connection.close()

if __name__ == '__main__':
    main()
