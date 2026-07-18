# 🏦 AI Financial Risk Analytics Platform

An end-to-end AI-powered financial risk analytics platform that predicts loan default probability, classifies customer risk, provides interactive business analytics, and supports batch prediction through an intuitive Streamlit web application.

## 🌐 Live Demo

🚀 **Live Application:** https://ai-financial-risk-analytics.streamlit.app/

---

# 📌 Project Overview

Financial institutions process thousands of loan applications every day. Manual risk assessment is time-consuming, inconsistent, and difficult to scale.

The **AI Financial Risk Analytics Platform** automates the loan risk assessment process using Machine Learning and Business Intelligence techniques.

The platform enables banks and financial organizations to:

- Predict loan default probability
- Classify customer risk
- Analyze customer financial behavior
- Process single and bulk loan applications
- Generate business insights through interactive dashboards

---

# ✨ Features

## 📊 Dashboard

- Business KPI Cards
- Customer Overview
- Loan Distribution
- Income Analysis
- Risk Distribution
- Interactive Charts

---

## 🤖 Loan Prediction

Predict loan default for an individual customer.

Features:

- Single customer prediction
- Default probability
- Risk classification
- Loan recommendation
- Real-time prediction

---

## 📈 Analytics

Interactive financial analytics including:

- Customer Segmentation
- Loan Analysis
- Income Analysis
- Risk Analytics
- Feature-based Insights
- Business Visualizations

---

## 📂 Batch Prediction

Upload a CSV file containing multiple customer records.

The application automatically:

- Cleans missing values
- Performs feature engineering
- Predicts default probability
- Classifies customer risk
- Generates prediction report
- Allows CSV export

---

## ℹ️ About

Project documentation including:

- Architecture
- Workflow
- Technologies Used
- Model Information

---

# 🏗 Project Workflow

```text
Historical Loan Dataset
            │
            ▼
Data Cleaning
            │
            ▼
Feature Engineering
            │
            ▼
Model Training
            │
            ▼
CatBoost Model
        (best_model.pkl)
            │
            ▼
────────────────────────────────────────────
            Deployment
────────────────────────────────────────────
            │
            ▼
      Streamlit Application
            │
            ├──────── Dashboard
            │
            ├──────── Loan Prediction
            │
            ├──────── Analytics
            │
            ├──────── Batch Prediction
            │
            ▼
     Financial Risk Assessment
```

---

# 👨‍💻 User Workflow

## Step 1

Open the application

https://ai-financial-risk-analytics.streamlit.app/

---

## Step 2

Choose one of the available modules.

- Dashboard
- Loan Prediction
- Analytics
- Batch Prediction

---

## Step 3

### Dashboard

View

- Total Customers
- Risk Distribution
- Financial KPIs
- Business Charts

---

### Loan Prediction

Enter customer information.

Click **Predict**.

The application:

- Validates inputs
- Performs preprocessing
- Generates prediction
- Calculates probability
- Displays recommendation

---

### Analytics

Explore

- Loan trends
- Customer behavior
- Financial insights
- Interactive charts

---

### Batch Prediction

Upload a CSV file.

The system automatically:

- Reads data
- Cleans missing values
- Performs feature engineering
- Predicts all customers
- Creates downloadable prediction report

---

# 🧠 Machine Learning Pipeline

Training Phase

```
Loan Dataset
      │
      ▼
Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Pipeline
      │
      ▼
CatBoost Classifier
      │
      ▼
best_model.pkl
```

Prediction Phase

```
User Input
      │
      ▼
Preprocessing Pipeline
      │
      ▼
CatBoost Model
      │
      ▼
Prediction Probability
      │
      ▼
Risk Classification
```

---

# 📁 Project Structure

```text
AI_Financial_Risk_Analytics/

│
├── app.py
├── requirements.txt
│
├── models/
│      best_model.pkl
│
├── data/
│      dashboard_data.csv
│      template_input.csv
│
├── pages/
│      1_Dashboard.py
│      2_Loan_Prediction.py
│      3_Analytics.py
│      4_Batch_Prediction.py
│      5_About.py
│
└── create_template.py
```

---

# 💻 Technology Stack

## Programming

- Python

## Machine Learning

- CatBoost
- Scikit-Learn
- Joblib

## Data Processing

- Pandas
- NumPy

## Visualization

- Plotly
- Matplotlib

## Web Framework

- Streamlit

---

# 📊 Model Information

| Model | CatBoost Classifier |
|--------|---------------------|
| Task | Binary Classification |
| Output | Loan Default Probability |
| Prediction | Risk Classification |

---

# 📂 Input

## Loan Prediction

Single customer details entered through the web interface.

---

## Batch Prediction

Upload CSV containing customer information.

---

# 📤 Output

The system provides:

- Default Probability
- Risk Category
- Recommendation
- Batch Prediction Report

---

# 📈 Business Use Cases

- Loan Approval Automation
- Credit Risk Assessment
- Customer Risk Profiling
- Financial Analytics
- Banking Decision Support
- Lending Risk Analysis

---

# 🚀 Deployment

The application is deployed using **Streamlit Community Cloud**.

Live Demo:

https://ai-financial-risk-analytics.streamlit.app/

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/saipranavchaitanya/AI_Financial_Risk_Analytics.git
```

Navigate to the project

```bash
cd AI_Financial_Risk_Analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🧪 Testing

The application has been tested for:

- Dashboard Loading
- Loan Prediction
- Analytics Visualization
- Batch Prediction
- CSV Upload
- Model Loading
- Prediction Generation
- Export Functionality

---

# 🔮 Future Enhancements

- Explainable AI (SHAP/LIME)
- Real-time Database Integration
- User Authentication
- REST API Support
- Cloud Database
- Automated Model Retraining
- Fraud Detection Module
- Credit Score Forecasting

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning
- Financial Risk Analytics
- Business Intelligence
- Streamlit Application Development
- Data Visualization
- Model Deployment
- Feature Engineering
- End-to-End ML Workflow

---

# 👤 Author

**A.N.S. Pranav Chaitanya**

B.Tech Computer Science Engineering

Aspiring Data Analytics 

GitHub:
https://github.com/saipranavchaitanya

LinkedIn:
https://www.linkedin.com/in/anspranavchaitanya

---

# 📄 License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, consider giving it a Star on GitHub!
