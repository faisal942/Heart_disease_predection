 # app.py
import streamlit as st
import login
import heart_disease

def main():
    # Initialize session state if it does not exist
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        heart_disease.heart_disease_prediction()
    else:
        login.login_page()

if __name__ == '__main__':
    main()
