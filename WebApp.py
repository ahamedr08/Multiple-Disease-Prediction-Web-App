import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Loading the saved models
diabetes_model = pickle.load(open('diabetes.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    st.header('Enter the details below:')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1, help="Number of times pregnant")
        SkinThickness = st.number_input('Skin Thickness value (mm)', min_value=0, max_value=100, help="Skinfold thickness measured in mm")
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', format="%.4f", help="Diabetes pedigree function")

    with col2:
        Glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=300, help="Blood glucose level in mg/dL")
        Insulin = st.number_input('Insulin Level (mu U/ml)', min_value=0, max_value=846, help="Insulin level in mu U/ml")
        Age = st.number_input('Age of the Person', min_value=1, max_value=120, help="Age in years")

    with col3:
        BloodPressure = st.number_input('Blood Pressure value (mm Hg)', min_value=0, max_value=200, help="Diastolic blood pressure in mm Hg")
        BMI = st.number_input('BMI value', format="%.2f", help="Body Mass Index")

    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    st.header('Enter the details below:')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=1, max_value=120, help="Age in years")
        sex = st.selectbox('Sex', options=['Male', 'Female'], help="Gender of the person")
        cp = st.number_input('Chest Pain types', min_value=0, max_value=3, help="Type of chest pain (0-3)")
        trestbps = st.number_input('Resting Blood Pressure (mm Hg)', min_value=0, max_value=200, help="Resting blood pressure in mm Hg")
        restecg = st.number_input('Resting Electrocardiographic results', min_value=0, max_value=2, help="Resting electrocardiographic results (0-2)")
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], help="Exercise induced angina (0: No, 1: Yes)")
        slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2, help="Slope of the peak exercise ST segment (0-2)")

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=0, max_value=600, help="Serum cholesterol in mg/dl")
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], help="Fasting blood sugar > 120 mg/dl (0: No, 1: Yes)")
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=0, max_value=220, help="Maximum heart rate achieved")
        oldpeak = st.number_input('ST depression induced by exercise', format="%.2f", help="ST depression induced by exercise")
        ca = st.number_input('Major vessels colored by flourosopy', min_value=0, max_value=3, help="Number of major vessels (0-3)")

    with col3:
        thal = st.selectbox('thal', options=['Normal', 'Fixed Defect', 'Reversible Defect'], help="Thalassemia (0: Normal, 1: Fixed defect, 2: Reversible defect)")

    # Mapping 'thal' to numeric values
    thal_dict = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}
    thal_numeric = thal_dict[thal]

    if st.button('Heart Disease Test Result'):
        user_input = [age, 1 if sex == 'Male' else 0, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal_numeric]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
        st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    st.header('Enter the details below:')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.number_input('MDVP: Fo(Hz)', format="%.3f", help="Average vocal fundamental frequency")
        Jitter_percent = st.number_input('MDVP: Jitter(%)', format="%.3f", help="Measure of frequency variation")
        RAP = st.number_input('MDVP: RAP', format="%.3f", help="Relative Amplitude Perturbation")
        Shimmer = st.number_input('MDVP: Shimmer', format="%.3f", help="Measure of amplitude variation")
        APQ3 = st.number_input('Shimmer: APQ3', format="%.3f", help="Three-point Amplitude Perturbation Quotient")
        HNR = st.number_input('HNR', format="%.3f", help="Harmonics-to-Noise Ratio")
        spread1 = st.number_input('spread1', format="%.3f", help="Nonlinear measure of fundamental frequency variation")

    with col2:
        fhi = st.number_input('MDVP: Fhi(Hz)', format="%.3f", help="Maximum vocal fundamental frequency")
        Jitter_Abs = st.number_input('MDVP: Jitter(Abs)', format="%.3f", help="Absolute measure of frequency variation")
        PPQ = st.number_input('MDVP: PPQ', format="%.3f", help="Five-point Period Perturbation Quotient")
        Shimmer_dB = st.number_input('MDVP: Shimmer(dB)', format="%.3f", help="Measure of amplitude variation in decibels")
        APQ5 = st.number_input('Shimmer: APQ5', format="%.3f", help="Five-point Amplitude Perturbation Quotient")
        RPDE = st.number_input('RPDE', format="%.3f", help="Recurrence Period Density Entropy")
        spread2 = st.number_input('spread2', format="%.3f", help="Nonlinear measure of fundamental frequency variation")

    with col3:
        flo = st.number_input('MDVP: Flo(Hz)', format="%.3f", help="Minimum vocal fundamental frequency")
        DDP = st.number_input('Jitter: DDP', format="%.3f", help="Difference of differences of periods")
        APQ = st.number_input('MDVP: APQ', format="%.3f", help="Amplitude Perturbation Quotient")
        DDA = st.number_input('Shimmer: DDA', format="%.3f", help="Difference of differences of amplitudes")
        NHR = st.number_input('NHR', format="%.3f", help="Noise-to-Harmonics Ratio")
        DFA = st.number_input('DFA', format="%.3f", help="Detrended Fluctuation Analysis")
        D2 = st.number_input('D2', format="%.3f", help="Dynamical complexity measure")

    with col4:
        PPE = st.number_input('PPE', format="%.3f", help="Pitch Period Entropy")

    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)
