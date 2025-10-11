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

## 🔄 Project Workflow

### 1. Data Preprocessing
- Checked for missing values; the dataset was complete with no nulls.
- Converted the `Date` column from string to datetime objects.
- Applied **one-hot encoding** to the categorical `Store` feature to prepare it for the model.
- Transformed the target variable `Weekly_Sales` using `np.log1p` to normalize its distribution.
- Selected key features for the model: `Holiday_Flag`, `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`, and the one-hot encoded store columns.

### 2. Model Building
- Utilized a **Linear Regression** model from Scikit-learn.
- The data was split into an 80% training set and a 20% testing set.
- The final trained model was saved as `model.pkl` using `pickle` for easy deployment.

### 3. Evaluation Metrics
- **Linear Regression Performance:**
  - R² Score: **0.96**
  - Mean Squared Error (MSE): **0.014**
  - Root Mean Squared Error (RMSE): **0.118**
- The model demonstrates a very high accuracy in predicting the log-transformed weekly sales.

### 4. Deployment
- The trained Linear Regression model was serialized using `pickle`.
- A **Streamlit web app** (`app.py`) was developed for user interaction.
- The app allows users to input details like the store number, holiday status, temperature, fuel price, CPI, and unemployment rate to receive an instant sales prediction.
- The output from the model is inverse-transformed using `np.expm1` to display the predicted sales in its original dollar value.
- The application can be deployed on platforms like **Streamlit Cloud, Heroku, or AWS** for broader access.

---
