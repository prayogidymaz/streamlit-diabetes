import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# judul web
st.title("Data Mining Prediksi Diabetes")

# membagi kolom
col1, col2 = st.columns(2)

with col1 :
    #Pregnancies = st.text_input ("Input nilai pregnancies")
    Pregnancies = float(st.text_input("Input nilai pregnancies") or 0)


with col2 :
    #Glucose = st.text_input ("Input nilai Glucose")
    Glucose = float(st.text_input("Input nilai glucose") or 0)


with col1 :
    #Bloodpressure = st.text_input ("Input nilai Bloodpressure")
    BloodPressure = float(st.text_input("Input nilai blood plessure") or 0)


with col2 :
    #SkinThickness = st.text_input ("Input nilai SkinThickness")
    SkinThickness = float(st.text_input("Input nilai skin thickness") or 0)


with col1 :
    #Insulin = st.text_input ("Input nilai Insulin")
    Insulin = float(st.text_input("Input nilai insulin") or 0)


with col2 :
    #BMI = st.text_input ("Input nilai BMI")
    BMI = float(st.text_input("Input nilai BMI") or 0)


with col1 :
    #DiabetesPedigreeFunction = st.text_input ("Input nilai Diabetes Pedigree Function")
    DiabetesPedigreeFunction = float(st.text_input("Input nilai diabetes pedigree function") or 0)


with col2 :
    #Age = st.text_input ("Input nilai Age")
    Age = float(st.text_input("Input nilai age") or 0)


# code untuk prediksi
diab_diagnosis = ""

# membuat tombol untuk prediksi
if st.button ("Test Prediksi Diabetes"):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 0):
        diab_diagnosis = "Pasien terkena Diabetes"
    else :
        diab_diagnosis = "Pasien tidak terkena Diabetes"
    st.success(diab_diagnosis)
