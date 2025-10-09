import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('Walmart Weekly Sales Prediction')
st.header('Enter the features to predict weekly sales')
holiday_flag = st.checkbox('Holiday Flag (1 for Holiday, 0 for Non-Holiday)')
temperature = st.slider('Temperature', min_value=-5.0, max_value=110.0, value=50.0)
fuel_price = st.slider('Fuel Price', min_value=2.0, max_value=4.5, value=3.0, step=0.01)
cpi = st.slider('CPI', min_value=120.0, max_value=230.0, value=190.0, step=0.1)
unemployment = st.slider('Unemployment', min_value=3.0, max_value=15.0, value=8.0, step=0.1)

stores = [f'Store_{i}' for i in range(2, 46)] 
selected_store = st.selectbox('Select Store', [f'Store_{i}' for i in range(1, 46)])

input_data = {
    'Holiday_Flag': int(holiday_flag),
    'Temperature': temperature,
    'Fuel_Price': fuel_price,
    'CPI': cpi,
    'Unemployment': unemployment
}

for store in stores:
    input_data[store] = False 
if selected_store != 'Store_1': 
    input_data[selected_store] = True
column_order = ['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment'] + stores

input_df = pd.DataFrame([input_data], columns=column_order)
for store in stores:
    input_df[store] = input_df[store].astype(bool)

if st.button('Predict Weekly Sales'):
    predicted_log_sales = model.predict(input_df)
    predicted_sales = np.expm1(predicted_log_sales) 

    st.header('Predicted Weekly Sales')
    st.write(f'The predicted weekly sales are: ${predicted_sales[0]:,.2f}')
