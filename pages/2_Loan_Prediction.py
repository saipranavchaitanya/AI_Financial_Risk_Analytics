import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Loan Default Prediction",
    page_icon="🏦",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#1565C0;
}

.sub-title{
    font-size:18px;
    color:#616161;
}

.section-title{
    font-size:22px;
    font-weight:bold;
    color:#0D47A1;
}

.metric-box{
    background:#F7F9FB;
    padding:12px;
    border-radius:10px;
}

</style>
""",unsafe_allow_html=True)

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    model_path=Path("models/best_model.pkl")

    return joblib.load(model_path)

model=load_model()

# ==========================================================
# LOAD TEMPLATE
# ==========================================================

@st.cache_data
def load_template():

    template_path=Path("data/template_input.csv")

    return pd.read_csv(template_path)

template=load_template()

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
'<p class="main-title">🏦 AI Financial Risk Analytics</p>',
unsafe_allow_html=True
)

st.markdown(
'<p class="sub-title">Loan Default Prediction using Machine Learning</p>',
unsafe_allow_html=True
)

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("Application")

st.sidebar.success("CatBoost Model")

st.sidebar.write("Input customer details to predict default probability.")

st.sidebar.info(f"Model Features : {template.shape[1]}")

st.sidebar.info("Prediction Type : Binary Classification")

# ==========================================================
# CUSTOMER FORM
# ==========================================================

left,right=st.columns(2)

with left:

    st.markdown(
    '<p class="section-title">👤 Personal Details</p>',
    unsafe_allow_html=True
    )

    gender=st.selectbox(
        "Gender",
        ["M","F"]
    )

    own_car=st.selectbox(
        "Own Car",
        ["N","Y"]
    )

    own_house=st.selectbox(
        "Own House",
        ["Y","N"]
    )

    age=st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    children=st.number_input(
        "Children",
        min_value=0,
        max_value=10,
        value=0
    )

    family_members=st.number_input(
        "Family Members",
        min_value=1,
        max_value=20,
        value=2
    )

    family_status=st.selectbox(
        "Family Status",
        [
            "Married",
            "Single / not married",
            "Civil marriage",
            "Separated",
            "Widow"
        ]
    )

    education=st.selectbox(
        "Education",
        [
            "Higher education",
            "Secondary / secondary special",
            "Incomplete higher",
            "Lower secondary",
            "Academic degree"
        ]
    )# ==========================================================
# FINANCIAL DETAILS
# ==========================================================

with right:

    st.markdown(
        '<p class="section-title">💰 Financial Details</p>',
        unsafe_allow_html=True
    )

    income = st.number_input(
        "Annual Income",
        min_value=10000.0,
        value=250000.0,
        step=1000.0
    )

    credit = st.number_input(
        "Credit Amount",
        min_value=1000.0,
        value=500000.0,
        step=1000.0
    )

    annuity = st.number_input(
        "Loan Annuity",
        min_value=1000.0,
        value=25000.0,
        step=100.0
    )

    goods_price = st.number_input(
        "Goods Price",
        min_value=1000.0,
        value=450000.0,
        step=1000.0
    )

    employment_years = st.number_input(
        "Employment Years",
        min_value=0.0,
        max_value=50.0,
        value=5.0,
        step=1.0
    )

    ext1 = st.slider(
        "External Score 1",
        0.0,
        1.0,
        0.50
    )

    ext2 = st.slider(
        "External Score 2",
        0.0,
        1.0,
        0.50
    )

    ext3 = st.slider(
        "External Score 3",
        0.0,
        1.0,
        0.50
    )

st.divider()

# ==========================================================
# ADDITIONAL INFORMATION
# ==========================================================

st.markdown(
    '<p class="section-title">🏢 Employment Information</p>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    income_type = st.selectbox(
        "Income Type",
        [
            "Working",
            "Commercial associate",
            "Pensioner",
            "State servant",
            "Student",
            "Businessman",
            "Maternity leave",
            "Unemployed"
        ]
    )

with col2:

    housing_type = st.selectbox(
        "Housing Type",
        [
            "House / apartment",
            "With parents",
            "Municipal apartment",
            "Rented apartment",
            "Office apartment",
            "Co-op apartment"
        ]
    )

with col3:

    contract_type = st.selectbox(
        "Contract Type",
        [
            "Cash loans",
            "Revolving loans"
        ]
    )

occupation = st.text_input(
    "Occupation (Optional)",
    value="Laborers"
)

organization = st.text_input(
    "Organization Type (Optional)",
    value="Business Entity Type 3"
)

st.divider()

# ==========================================================
# VALIDATION
# ==========================================================

if income <= 0:
    st.error("Income must be greater than zero.")

if credit <= 0:
    st.error("Credit amount must be greater than zero.")

if goods_price <= 0:
    st.error("Goods price must be greater than zero.")

if annuity <= 0:
    st.error("Annuity must be greater than zero.")

# ==========================================================
# PREDICT BUTTON
# ==========================================================

predict = st.button(
    "🚀 Predict Loan Default",
    use_container_width=True
)

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def safe_divide(a, b):
    if b == 0:
        return 0
    return a / b


def calculate_age_days(age):
    return -(age * 365)


def calculate_employment_days(years):
    return -(years * 365)


def risk_level(probability):

    if probability < 0.30:
        return (
            "🟢 LOW RISK",
            "Loan can be approved."
        )

    elif probability < 0.60:
        return (
            "🟡 MEDIUM RISK",
            "Manual verification is recommended."
        )

    else:
        return (
            "🔴 HIGH RISK",
            "Loan approval is not recommended."
        )
# ==========================================================
# PREDICTION ENGINE
# ==========================================================

if predict:

    try:

        # -----------------------------------------------
        # COPY TEMPLATE
        # -----------------------------------------------

        input_df = template.copy()

        # -----------------------------------------------
        # PERSONAL DETAILS
        # -----------------------------------------------

        input_df.loc[0, "CODE_GENDER"] = gender
        input_df.loc[0, "FLAG_OWN_CAR"] = own_car
        input_df.loc[0, "FLAG_OWN_REALTY"] = own_house

        input_df.loc[0, "CNT_CHILDREN"] = children
        input_df.loc[0, "CNT_FAM_MEMBERS"] = family_members

        input_df.loc[0, "NAME_FAMILY_STATUS"] = family_status
        input_df.loc[0, "NAME_EDUCATION_TYPE"] = education

        # -----------------------------------------------
        # FINANCIAL DETAILS
        # -----------------------------------------------

        input_df.loc[0, "AMT_INCOME_TOTAL"] = income
        input_df.loc[0, "AMT_CREDIT"] = credit
        input_df.loc[0, "AMT_ANNUITY"] = annuity
        input_df.loc[0, "AMT_GOODS_PRICE"] = goods_price

        # -----------------------------------------------
        # EMPLOYMENT DETAILS
        # -----------------------------------------------

        input_df.loc[0, "NAME_INCOME_TYPE"] = income_type
        input_df.loc[0, "NAME_HOUSING_TYPE"] = housing_type
        input_df.loc[0, "NAME_CONTRACT_TYPE"] = contract_type

        input_df.loc[0, "OCCUPATION_TYPE"] = occupation
        input_df.loc[0, "ORGANIZATION_TYPE"] = organization

        # -----------------------------------------------
        # EXTERNAL SCORES
        # -----------------------------------------------

        input_df.loc[0, "EXT_SOURCE_1"] = ext1
        input_df.loc[0, "EXT_SOURCE_2"] = ext2
        input_df.loc[0, "EXT_SOURCE_3"] = ext3

        # -----------------------------------------------
        # DATE FEATURES
        # -----------------------------------------------

        input_df.loc[0, "DAYS_BIRTH"] = calculate_age_days(age)
        input_df.loc[0, "DAYS_EMPLOYED"] = calculate_employment_days(
            employment_years
        )

        # -----------------------------------------------
        # ENGINEERED FEATURES
        # -----------------------------------------------

        input_df.loc[0, "AGE_YEARS"] = age

        input_df.loc[0, "EMPLOYMENT_YEARS"] = employment_years

        input_df.loc[0, "CREDIT_INCOME_RATIO"] = safe_divide(
            credit,
            income
        )

        input_df.loc[0, "ANNUITY_INCOME_RATIO"] = safe_divide(
            annuity,
            income
        )

        input_df.loc[0, "GOODS_CREDIT_RATIO"] = safe_divide(
            goods_price,
            credit
        )

        # -----------------------------------------------
        # OPTIONAL FEATURES
        # Only update if present in template
        # -----------------------------------------------

        optional_values = {
            "DAYS_REGISTRATION": -3650,
            "DAYS_ID_PUBLISH": -2500,
            "OWN_CAR_AGE": 0,
            "OBS_30_CNT_SOCIAL_CIRCLE": 0,
            "DEF_30_CNT_SOCIAL_CIRCLE": 0,
            "OBS_60_CNT_SOCIAL_CIRCLE": 0,
            "DEF_60_CNT_SOCIAL_CIRCLE": 0,
            "AMT_REQ_CREDIT_BUREAU_YEAR": 0
        }

        for column, value in optional_values.items():
            if column in input_df.columns:
                input_df.loc[0, column] = value

        # -----------------------------------------------
        # CHECK FOR MISSING VALUES
        # -----------------------------------------------

        missing = input_df.isnull().sum().sum()

        if missing > 0:
            st.warning(
                f"{missing} missing values detected. "
                "The model will use template defaults where applicable."
            )

        # -----------------------------------------------
        # MODEL PREDICTION
        # -----------------------------------------------

        probability = model.predict_proba(input_df)[0][1]
        prediction = model.predict(input_df)[0]

        risk, recommendation = risk_level(probability)        # -----------------------------------------------
        # DISPLAY RESULTS
        # -----------------------------------------------

        st.divider()

        st.success("✅ Prediction Completed Successfully")

        # ==================================================
        # KPI CARDS
        # ==================================================

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Default Probability",
                f"{probability * 100:.2f}%"
            )

        with col2:
            st.metric(
                "Prediction",
                "Default" if prediction == 1 else "Non Default"
            )

        with col3:
            st.metric(
                "Risk Level",
                risk
            )

        st.divider()

        # ==================================================
        # RISK METER
        # ==================================================

        st.subheader("📊 Risk Score")

        st.progress(float(probability))

        st.write(f"Risk Score : **{probability:.2%}**")

        # ==================================================
        # RECOMMENDATION
        # ==================================================

        st.subheader("💡 Recommendation")

        if prediction == 0:

            st.success(recommendation)

        else:

            st.error(recommendation)

        # ==================================================
        # CUSTOMER SUMMARY
        # ==================================================

        st.subheader("📋 Customer Summary")

        summary = pd.DataFrame({

            "Field":[
                "Gender",
                "Age",
                "Income",
                "Credit",
                "Annuity",
                "Goods Price",
                "Employment Years",
                "Children",
                "Family Members",
                "Education",
                "Family Status"
            ],

            "Value":[
                gender,
                age,
                income,
                credit,
                annuity,
                goods_price,
                employment_years,
                children,
                family_members,
                education,
                family_status
            ]

        })

        st.dataframe(
            summary,
            use_container_width=True
        )

        # ==================================================
        # DOWNLOAD REPORT
        # ==================================================

        report = pd.DataFrame({

            "Prediction":[
                "Default" if prediction==1 else "Non Default"
            ],

            "Probability":[
                round(probability*100,2)
            ],

            "Risk":[
                risk
            ],

            "Recommendation":[
                recommendation
            ]

        })

        csv = report.to_csv(index=False).encode("utf-8")

        st.download_button(

            label="📥 Download Prediction Report",

            data=csv,

            file_name="loan_prediction_report.csv",

            mime="text/csv"

        )

        # ==================================================
        # MODEL INFORMATION
        # ==================================================

        with st.expander("ℹ Model Information"):

            st.write("Model : CatBoost Classifier")

            st.write("Task : Loan Default Prediction")

            st.write(f"Features Used : {template.shape[1]}")

            st.write("Pipeline : Scikit-learn Pipeline")

            st.write("Prediction : Binary Classification")

    except Exception as e:

        st.error("Prediction Failed")

        st.exception(e)