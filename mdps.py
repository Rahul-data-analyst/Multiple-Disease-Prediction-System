# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:12:40 2023

@author: rahul
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_model = pickle.load(open('heart_disease_model.sav','rb'))

breastCancer_model = pickle.load(open('breastCancer_model.sav','rb'))



# sidebar for navigate 

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction', 
                            'Breast Cancer Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    
# Diabetes Prediction page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction Using ML')
    
    # input fields
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Presure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    
    #For prediction
    diab_diagnosis = ''
    
    #creating button for prediction
    if st.button('Diabetes Test Result'):
         diab_prediction= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI, DiabetesPedigreeFunction,Age]])
    
         if(diab_prediction[0]==0):
             diab_diagnosis = 'The person is not Diabetic'
        
         else:
             diab_diagnosis = "The person is Diabetic"
             
    st.success(diab_diagnosis)
    
# heart disease prediction page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Using ML')
    
    #input fields 
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
       
    
   # code for Prediction
    heart_diagnosis = ''
   
   # creating a button for Prediction
   
    if st.button('Heart Disease Test Result'):
       heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
       
       if (heart_prediction[0] == 1):
         heart_diagnosis = 'The person is having heart disease'
       else:
         heart_diagnosis = 'The person does not have any heart disease'
       
    st.success(heart_diagnosis)
    
    
# breast cancer disease prediction page
if (selected == 'Breast Cancer Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction Using ML')
    
    #input fields 
    radius_mean = st.text_input('Mean Radius')
    texture_mean = st.text_input('Mean Texture')
    perimeter_mean = st.text_input('Mean Perimeter')
    area_mean = st.text_input('Mean Area')
    smoothness_mean = st.text_input('Mean Smoothness')
    compactness_mean = st.text_input('Mean Compactness')
    concavity_mean = st.text_input('Mean Concavity')
    concave_points_mean = st.text_input('Mean Concave Points')
    symmetry_mean = st.text_input('Mean Symmetry')
    fractal_dimension_mean = st.text_input('Mean Fractal Dimension')
    radius_error = st.text_input('Radius Error')
    texture_error = st.text_input('Texture Error')
    perimeter_error = st.text_input('Perimeter Error')
    area_error = st.text_input('Area Error')
    smoothness_error = st.text_input('Smoothness Error')
    compactness_error = st.text_input('Compactness Error')
    concavity_error = st.text_input('Concavity Error')
    concave_point_error = st.text_input('Concave Point Error')
    symmetry_error = st.text_input('Symmetry Error')
    symmetry_mean = st.text_input('symmetry_mean')
    fractal_dimension_error = st.text_input('fractal_dimension_error')
    worst_radius = st.text_input('worst_radius')
    worst_texture = st.text_input('Worst Texture')
    worst_perimeter = st.text_input('Worst Perimeter')
    worst_area = st.text_input('Worst Area')
    worst_smoothless = st.text_input('Worst Smoothless')
    worst_compactness = st.text_input('Worst Compactness')
    worst_concavity = st.text_input('Worst Concavity')
    worst_concave_points = st.text_input('Worst Concave Points')
    worst_symmetry = st.text_input('Worst Symmetry')
    worst_fractal_dimension = st.text_input('Worst Fractal Dimension')


   # code for Prediction
    breastCancer_diagnosis = ''
   
   # creating a button for Prediction
   
    if st.button('Breast Cancer Disease Test Result'):
       breastCancer_prediction = breastCancer_model.predict([[radius_mean,	texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_point_error,symmetry_error,symmetry_mean,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothless,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])                          
       
       if (breastCancer_prediction[0] == 'B'):
          breastCancer_diagnosis = 'The Breast cancer is Benign'
       else:
          breastCancer_diagnosis = 'The Breast cancer is Malignant'
       
    st.success(breastCancer_diagnosis)


    
