# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:38:19 2024

@author: sampa
"""

import pickle
import streamlit as st
#from streamlit_option_menu import option_menu

loaded_model = pickle.load(open('trained_model.sav','rb'))

st.title('Diabetes Prediction')
    
    #Getting input data from user.
    # columns for input field
    
col1, col2, col3 = st.columns(3)
    
with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
with col2:
    Glucose = st.text_input('Glucose Level')
        
with col3:    
    BloodPressure = st.text_input('Blood Pressure value')
    
with col1:    
    SkinThickness = st.text_input('Skin Thickness value')
    
with col2:    
    Insulin = st.text_input('Insulin Level')
        
with col3:    
    BMI = st.text_input('BMI Value')
        
with col1:    
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
        
with col2:    
    Age = st.text_input('Age of the person')
    

# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):

    user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                  BMI, DiabetesPedigreeFunction, Age]

    user_input = [float(x) for x in user_input]

    diab_prediction = loaded_model.predict([user_input])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'

st.success(diab_diagnosis)    
    
    
   
    
    
