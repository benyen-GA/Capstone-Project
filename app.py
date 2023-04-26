import streamlit as st
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import joblib
import xgboost

st.title("Vehicle Insurance Fraud Detection")
Month = st.selectbox('Month of claim',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Make = st.selectbox('Car Make',('Accura', 'BMW', 'Chevrolet', 'Dodge', 'Ferrari', 'Ford', 'Honda', 'Jaguar', 'Lexus', 'Mazda', 'Mecedes', 'Mercury', 'Nisson', 'Pontiac', 'Porche', 'Saab', 'Saturn', 'Toyota', 'VW'))
AccidentArea = st.selectbox('Area of Accident',('Rural', 'Urban'))
Sex = st.selectbox('Gender',('Female', 'Male'))
Age = st.number_input('Age of person claiming',min_value=16, max_value = 80)
Fault = st.selectbox('Party at Fault',('Policy Holder', 'Third Party'))
VehicleCategory = st.selectbox('Vehicle Category',('Sedan', 'Sport', 'Utility'))
Deductible = st.selectbox('what is your current excess',('300', '400', '500', '700'))
PastNumberOfClaims = st.selectbox('Have you claim previously with the company?',('1', '2 to 4', 'more than 4', 'none'))
AgeOfPolicyHolder = st.selectbox('What is the age of the policy holder?',('16 to 17', '18 to 20', '21 to 25', '26 to 30', '31 to 35', '36 to 40', '41 to 50', '51 to 65', 'over 65'))
PoliceReportFiled = st.selectbox('Is a police report being filed?',('No','Yes'))
AgentType = st.selectbox('What type of Agent is servicing your policy?', ('External','Internal'))
NumberOfSuppliments = st.selectbox('Any extras services included in the policy?',('none','1 to 2', '3 to 5', 'more than 5'))
AddressChange_Claim = st.selectbox('Is there any change in the original address of the policy?',('no change', 'under 6 months','1 year', '2 to 3 years', '4 to 8 years'))
BasePolicy = st.selectbox('What is the type of Policy?', ('All Perils', 'Collision', 'Liability'))
AgeOfVehicle = st.selectbox('How old is the vehicle of claim?',('new','2 years', '3 years', '4 years', '5 years', '6 years', '7 years', 'more than 7'))





if st.button('Predict'):
    model = joblib.load('xgb_model.joblib')
    X = pd.DataFrame([['Month','Make','AccidentArea','Sex','Age','Fault',
                       'VehicleCategory','Deductible','PastNumberOfClaims',
                       'AgeOfPolicyHolder','PoliceReportFiled','AgentType',
                       'NumberOfSuppliments','AddressChange_Claim','BasePolicy',
                       'AgeOfVehicle']], columns = ['Month','Make','AccidentArea','Sex','Age','Fault',
                       'VehicleCategory','Deductible','PastNumberOfClaims',
                       'AgeOfPolicyHolder','PoliceReportFiled','AgentType',
                       'NumberOfSuppliments','AddressChange_Claim','BasePolicy',
                       'AgeOfVehicle'] )
    # assuming your DataFrame is called `df`
    object_cols = X.select_dtypes(include=['object'])

    # change the dtype of each object column to categorical
    for col in object_cols:
        X[col] = X[col].astype('category')
   
    threshold = 0.05
    pred_prob = model.predict_proba(X)[0][1]
    pred = 1 if pred_prob > threshold else 0
    st.markdown(f'### The insurance claim is {pred}')