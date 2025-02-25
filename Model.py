import pandas as pd
import streamlit as st
import pickle

loaded_model = pickle.load(open ('trained_model.sav', 'rb'))
def heartdisease_prediction (input_data):
        # changing the input data to a numpy array
        Array_data= np.asarray(input_data)
        
        #Reshaping the numpy array to a 1D ARRAY as we are predicting for only one instance
        reshaped_data = Array_data.reshape (1,-1)
        prediction = loaded_model.predict(reshaped_data)
        #using if else logic to determine heart disease is true or not
        if (prediction[0] == 0):
            st.success ('The person does not have heart disease')
        else:
            st.warning ('The person have heart disease')
        #Adding title to the page
        st.title ('Heart Disease Prediction Web Application')

        #Getting the input data from the user 
        #AND storing it in same column names as used in the Dataset 
        age = st.text_input("Enter your Age in Years")
        sex = st.text_input ("Choose Sex: 1 is for male, 0 is for female")
        cp = st.text_input ("Choose Chest pain type(0 or 1)")
        trestbps = st.text_input ("Input Resting blood pressure in mm Hg:")
        chol = st.text_input ("Enter Serum cholesterol in mg/dl")
        fbs = st.text_input ("Is Your Fasting blood sugar > 120 mg/dl :Then 1 – true, 0 – false")
        restecg = st.text_input ("Resting electrocardiographic results(0 or 1 or 2)")
        thalach = st.text_input ("Maximum heart rate achieved")
        exang = st.text_input ("Do You Have Exercise induced angina: 1 – yes, 0 – no")
        oldpeak = st.text_input ("Enter ST depression in mm")
        slope = st.text_input ("Enter Slope")
        ca = st.text_input ("Number of major vessels (0-3)")
        thal = st.text_input ("Enter thalach:")
        
        # code for Prediction
        diagnosis = " "
        # creating a button for Prediction
        if st.button ("Heart Disease Test Result"):
            diagnosis = heartdisease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,that])
