# Loan Approval Prediction App

This is a web-based machine learning application that predicts whether a loan will be approved or not based on user inputs such as income, credit history, employment status, and more.

Built using:
- Streamlit for the frontend
- scikit-learn for the machine learning model
- Logistic Regression for prediction

##  Demo

[Live App](https://loanprediction-meiobjfwcpnircz8wd2dhc.streamlit.app/)

---

##  Features

- Simple web interface to input applicant details
- Predicts loan approval instantly
- Based on a trained Logistic Regression model
- Clean and responsive interface using Streamlit

---

##  Input Fields

- Gender  
- Marital Status  
- Number of Dependents  
- Education  
- Self Employment  
- Applicant Income  
- Coapplicant Income  
- Loan Amount  
- Loan Term  
- Credit History  
- Property Area  

---

##  Machine Learning

- Trained using the [Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
- Model: Logistic Regression
- Input features were label-encoded and preprocessed for consistency

---

##  Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/loan-prediction-app.git
cd loan-prediction-app
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the app locally
```bash
python -m streamlit run loan_app.py
```

---

## License
This project is open-source and available under the MIT License.

