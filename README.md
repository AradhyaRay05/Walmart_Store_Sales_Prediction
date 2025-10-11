# 🛒 Walmart Store Sales Prediction  - Predicting Walmart's weekly sales

---

## 📌 Project Goal
The goal of this project is to build a machine learning model that accurately predicts the weekly sales for Walmart stores. By leveraging historical data on sales, store characteristics, and economic indicators, the application provides a reliable tool for forecasting, aiding in better inventory management, staffing decisions, and promotional planning.

---

## 📖 Project Overview
This project presents an end-to-end machine learning solution for predicting Walmart's weekly sales:

- **Data Preprocessing and Analysis:** The dataset is cleaned, and an Exploratory Data Analysis (EDA) is performed to uncover relationships between features and weekly sales.
- **Feature Engineering:** Categorical features like `Store` are one-hot encoded, and the `Date` column is converted to a datetime format for analysis. The target variable, `Weekly_Sales`, is log-transformed to handle its right-skewed distribution.
- **Model Building:** A **Linear Regression** model is trained on the preprocessed data to predict the log-transformed weekly sales.
- **Deployment:** The trained model is deployed as an interactive web application using **Streamlit**, allowing users to get sales predictions in real-time.

---
