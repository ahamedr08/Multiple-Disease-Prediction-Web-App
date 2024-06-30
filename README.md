# Health Assistant - Multiple Disease Prediction System

Welcome to the **Health Assistant** application, a multiple disease prediction system using machine learning. This app allows users to predict the likelihood of having diabetes, heart disease, or Parkinson's disease based on their input data. The application is built using Streamlit and utilizes machine learning models trained to provide accurate predictions.

## Overview
The Health Assistant application is designed to assist users in predicting the probability of having certain diseases. The app features:
- **Diabetes Prediction**
- **Heart Disease Prediction**
- **Parkinson's Disease Prediction**

Each prediction is made using a separate machine learning model trained on relevant datasets.

## Usage
Once the app is running, you can navigate between different prediction pages using the sidebar menu:
- **Diabetes Prediction**: Enter details such as pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age to get a prediction.
- **Heart Disease Prediction**: Provide details including age, sex, chest pain type, resting blood pressure, serum cholesterol, fasting blood sugar, resting electrocardiographic results, maximum heart rate achieved, exercise induced angina, oldpeak, slope, major vessels colored by fluoroscopy, and thalassemia type for prediction.
- **Parkinson's Disease Prediction**: Input vocal measurements such as MDVP (Fo, Fhi, Flo), jitter, shimmer, noise-to-harmonics ratio, recurrence period density entropy, detrended fluctuation analysis, and pitch period entropy to get a prediction.

## Model Accuracy
The accuracy of the models on both training and test data is as follows:

### Diabetes Prediction (SVM)
- **Training Data Accuracy**: 78.66%
- **Test Data Accuracy**: 77.27%

### Heart Disease Prediction (Logistic Regression)
- **Training Data Accuracy**: 85.12%
- **Test Data Accuracy**: 81.97%

### Parkinson's Disease Prediction (SVM)
- **Training Data Accuracy**: 88.46%
- **Test Data Accuracy**: 87.18%

## Web Application
You can access the live web application [here](https://ahamedr08.streamlit.app/).

Feel free to reach out with any questions or feedback! Happy predicting!
