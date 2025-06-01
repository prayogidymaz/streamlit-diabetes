import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# judul web
st.title("Data Mining Prediksi Diabetes")

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ("Input nilai pregnancies")

with col2 :
    Glucose = st.text_input ("Input nilai Glucose")

with col1 :
    Bloodpressure = st.text_input ("Input nilai Bloodpressure")

with col2 :
    SkinThickness = st.text_input ("Input nilai SkinThickness")

with col1 :
    Insulin = st.text_input ("Input nilai Insulin")

with col2 :
    BMI = st.text_input ("Input nilai BMI")

with col1 :
    DiabetesPedigreeFunction = st.text_input ("Input nilai Diabetes Pedigree Function")

with col2 :
    Age = st.text_input ("Input nilai Age")

# code untuk prediksi
diab_diagnosis = ""

# membuat tombol untuk prediksi
if st.button ("Test Prediksi Diabetes"):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 0):
        diab_diagnosis = "Pasien terkena Diabetes"
    else :
        diab_diagnosis = "Pasien tidak terkena Diabetes"
    st.success(diab_diagnosis)