import streamlit as st

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# ==========================================================
# HEADER
# ==========================================================

st.title("ℹ️ About AI Financial Risk Analytics Platform")

st.write(
    """
This project is an AI-powered Financial Risk Analytics Platform
developed using Machine Learning and Business Intelligence tools.

The application predicts loan default probability,
analyzes customer risk,
visualizes banking insights,
and supports batch prediction.
"""
)

st.divider()

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.header("📌 Project Overview")

st.markdown("""
### Objective

The objective of this project is to assist financial institutions
in identifying high-risk loan applicants using Artificial Intelligence.

The platform provides

- Loan Default Prediction
- Financial Risk Dashboard
- Customer Analytics
- Batch Prediction
- Business Insights

to improve lending decisions.
""")

st.divider()

# ==========================================================
# PROJECT WORKFLOW
# ==========================================================

st.header("⚙️ Project Workflow")

st.markdown("""
1. Data Collection

↓

2. Data Cleaning

↓

3. Feature Engineering

↓

4. Model Training

↓

5. Model Evaluation

↓

6. Deployment using Streamlit

↓

7. Loan Prediction

↓

8. Business Analytics

↓

9. Batch Prediction

↓

10. Decision Support
""")

st.divider()

# ==========================================================
# DATASET
# ==========================================================

st.header("📂 Dataset")

st.write("""
Dataset Used

Home Credit Default Risk Dataset

Features include

• Customer Information

• Income

• Credit Amount

• Loan Annuity

• Family Information

• Education

• Employment

• External Credit Scores

• Loan Default Target
""")# ==========================================================
# MACHINE LEARNING PIPELINE
# ==========================================================

st.header("🤖 Machine Learning Pipeline")

st.markdown("""
### Data Preprocessing

✔ Missing Value Handling

✔ Feature Engineering

✔ Ratio Features

✔ Encoding

✔ Scaling

### Algorithms Evaluated

• Logistic Regression

• Random Forest

• XGBoost

• LightGBM

• CatBoost

### Selected Model

🏆 CatBoost Classifier
""")

st.divider()

# ==========================================================
# PROJECT FEATURES
# ==========================================================

st.header("🚀 Features")

features = [

    "AI Loan Default Prediction",

    "Interactive Dashboard",

    "Advanced Analytics",

    "Batch Prediction",

    "Risk Classification",

    "Business Insights",

    "CSV Download",

    "Executive Reports",

    "Interactive Plotly Charts",

    "Machine Learning Pipeline"

]

for feature in features:

    st.success(feature)

st.divider()

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.header("🛠 Technology Stack")

tech1, tech2, tech3 = st.columns(3)

with tech1:

    st.subheader("Programming")

    st.write("""
Python

Pandas

NumPy
""")

with tech2:

    st.subheader("Machine Learning")

    st.write("""
Scikit-Learn

CatBoost

Joblib
""")

with tech3:

    st.subheader("Visualization")

    st.write("""
Streamlit

Plotly

Matplotlib
""")

st.divider()# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

st.header("📈 Model Performance")

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.metric("Model", "CatBoost")

with metric2:

    st.metric("Task", "Classification")

with metric3:

    st.metric("Deployment", "Streamlit")

with metric4:

    st.metric("Dataset", "Home Credit")

st.info("""
Add your actual evaluation metrics here after model training.

Example

Accuracy

Precision

Recall

F1 Score

ROC-AUC
""")

st.divider()

# ==========================================================
# FUTURE IMPROVEMENTS
# ==========================================================

st.header("🚀 Future Enhancements")

future = [

    "Fraud Detection",

    "Customer Segmentation",

    "Loan Recommendation System",

    "Real-Time API Integration",

    "Cloud Deployment",

    "SHAP Explainability",

    "Credit Score Prediction",

    "Automated Report Generation"

]

for item in future:

    st.write("✅", item)

st.divider()

# ==========================================================
# DEVELOPER
# ==========================================================

st.header("👨‍💻 Developer")

st.write("""

AI Financial Risk Analytics Platform

Developed as an end-to-end Machine Learning project.

Technologies

Python

Machine Learning

Data Analytics

Business Intelligence

Streamlit

Plotly

CatBoost

Scikit-Learn

""")

st.divider()

st.success("🎉 Thank you for using AI Financial Risk Analytics Platform.")