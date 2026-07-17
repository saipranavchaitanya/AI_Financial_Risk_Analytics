import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import time

from pathlib import Path
from datetime import datetime

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📁",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main-title{
font-size:38px;
font-weight:bold;
color:#1E3A8A;
}

.section-title{
font-size:24px;
font-weight:bold;
color:#0F172A;
}

.card{
background-color:#F8FAFC;
padding:18px;
border-radius:12px;
border:1px solid #E2E8F0;
margin-bottom:10px;
}

</style>
""",unsafe_allow_html=True)

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    return joblib.load("models/best_model.pkl")


model = load_model()

# ==========================================================
# LOAD TEMPLATE
# ==========================================================

@st.cache_data
def load_template():

    return pd.read_csv(
        "data/template_input.csv"
    )


template = load_template()

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
"""
<div class='main-title'>
📁 Batch Loan Default Prediction
</div>
""",
unsafe_allow_html=True
)

st.write(
"""
Upload a CSV file containing multiple customers.

The AI model will automatically:

✔ Validate the dataset

✔ Clean missing values

✔ Perform feature engineering

✔ Predict loan default probability

✔ Classify customer risk

✔ Generate analytics

✔ Export prediction results
"""
)

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🏦 Batch Prediction")

st.sidebar.success("Model : CatBoost")

st.sidebar.info(
    f"Expected Features : {template.shape[1]}"
)

st.sidebar.markdown("---")

st.sidebar.write("### Prediction Workflow")

st.sidebar.write("""
1️⃣ Upload CSV

2️⃣ Validate Dataset

3️⃣ Feature Engineering

4️⃣ AI Prediction

5️⃣ Risk Analysis

6️⃣ Download Results
""")

st.sidebar.markdown("---")

st.sidebar.write("Pipeline")

st.sidebar.code("""
CSV

↓

Validation

↓

Prediction

↓

Analytics
""")

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📂 Upload Customer CSV",
    type=["csv"]
)

if uploaded_file is None:

    st.info(
        "Please upload a CSV file to continue."
    )

    st.stop()

# ==========================================================
# LOAD CSV
# ==========================================================

try:

    upload_df = pd.read_csv(
        uploaded_file
    )

except Exception as e:

    st.error(e)

    st.stop()

# ==========================================================
# SUCCESS MESSAGE
# ==========================================================

st.success(
    f"✅ {len(upload_df):,} records uploaded successfully."
)

# ==========================================================
# DATASET SUMMARY
# ==========================================================

st.markdown("## 📊 Uploaded Dataset Summary")

c1,c2,c3,c4=st.columns(4)

with c1:

    st.metric(
        "Rows",
        f"{upload_df.shape[0]:,}"
    )

with c2:

    st.metric(
        "Columns",
        upload_df.shape[1]
    )

with c3:

    memory=upload_df.memory_usage(
        deep=True
    ).sum()/1024

    st.metric(
        "Memory",
        f"{memory:.1f} KB"
    )

with c4:

    st.metric(
        "Expected Features",
        template.shape[1]
    )

st.divider()

# ==========================================================
# DATA PREVIEW
# ==========================================================

st.subheader("📄 Uploaded Dataset Preview")

st.dataframe(
    upload_df.head(10),
    use_container_width=True,
    height=350
)

st.divider()# ==========================================================
# DATASET VALIDATION
# ==========================================================

st.markdown("## ✅ Dataset Validation")

required_columns = [
    "CODE_GENDER",
    "FLAG_OWN_CAR",
    "FLAG_OWN_REALTY",
    "CNT_CHILDREN",
    "CNT_FAM_MEMBERS",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "AMT_GOODS_PRICE",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "NAME_INCOME_TYPE",
    "NAME_HOUSING_TYPE",
    "NAME_CONTRACT_TYPE",
    "OCCUPATION_TYPE",
    "ORGANIZATION_TYPE",
    "EXT_SOURCE_1",
    "EXT_SOURCE_2",
    "EXT_SOURCE_3",
    "AGE_YEARS",
    "EMPLOYMENT_YEARS"
]

missing_columns = [
    col for col in required_columns
    if col not in upload_df.columns
]

if missing_columns:

    st.error("❌ Required columns are missing.")

    st.write("Missing Columns:")

    st.write(missing_columns)

    st.stop()

else:

    st.success("✅ Dataset validation completed successfully.")

st.divider()

# ==========================================================
# DATA QUALITY REPORT
# ==========================================================

st.markdown("## 📊 Data Quality Report")

total_missing = upload_df.isnull().sum().sum()

duplicate_rows = upload_df.duplicated().sum()

numeric_columns = upload_df.select_dtypes(
    include=["int64","float64"]
).columns

categorical_columns = upload_df.select_dtypes(
    include=["object"]
).columns

q1,q2,q3,q4 = st.columns(4)

with q1:

    st.metric(
        "Missing Values",
        f"{total_missing:,}"
    )

with q2:

    st.metric(
        "Duplicate Rows",
        duplicate_rows
    )

with q3:

    st.metric(
        "Numeric Columns",
        len(numeric_columns)
    )

with q4:

    st.metric(
        "Categorical Columns",
        len(categorical_columns)
    )

st.divider()

# ==========================================================
# DATA CLEANING
# ==========================================================

st.markdown("## 🧹 Data Cleaning")

status = st.empty()

status.info("Cleaning missing values...")

for col in numeric_columns:

    upload_df[col] = upload_df[col].fillna(
        upload_df[col].median()
    )

for col in categorical_columns:

    if upload_df[col].isnull().sum() > 0:

        upload_df[col] = upload_df[col].fillna(
            upload_df[col].mode()[0]
        )

status.success("✅ Missing values handled successfully.")

st.divider()

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

st.markdown("## ⚙️ Feature Engineering")

def safe_divide(a, b):

    if pd.isna(a) or pd.isna(b):

        return 0

    if b == 0:

        return 0

    return a / b

status = st.empty()

status.info("Creating engineered features...")

upload_df["CREDIT_INCOME_RATIO"] = upload_df.apply(
    lambda x: safe_divide(
        x["AMT_CREDIT"],
        x["AMT_INCOME_TOTAL"]
    ),
    axis=1
)

upload_df["ANNUITY_INCOME_RATIO"] = upload_df.apply(
    lambda x: safe_divide(
        x["AMT_ANNUITY"],
        x["AMT_INCOME_TOTAL"]
    ),
    axis=1
)

upload_df["GOODS_CREDIT_RATIO"] = upload_df.apply(
    lambda x: safe_divide(
        x["AMT_GOODS_PRICE"],
        x["AMT_CREDIT"]
    ),
    axis=1
)

if "DAYS_BIRTH" not in upload_df.columns:

    upload_df["DAYS_BIRTH"] = (
        upload_df["AGE_YEARS"] * -365
    )

if "DAYS_EMPLOYED" not in upload_df.columns:

    upload_df["DAYS_EMPLOYED"] = (
        upload_df["EMPLOYMENT_YEARS"] * -365
    )

status.success("✅ Feature engineering completed.")

st.divider()

# ==========================================================
# FEATURE SUMMARY
# ==========================================================

st.markdown("## 📈 Engineered Features")

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.metric(
        "Credit / Income",
        "Created"
    )

with feature2:

    st.metric(
        "Annuity / Income",
        "Created"
    )

with feature3:

    st.metric(
        "Goods / Credit",
        "Created"
    )

st.divider()

# ==========================================================
# PROCESSED DATASET
# ==========================================================

st.markdown("## 📄 Processed Dataset Preview")

st.dataframe(
    upload_df.head(10),
    use_container_width=True,
    height=350
)

st.divider()

# ==========================================================
# READY FOR PREDICTION
# ==========================================================

st.success("""
### ✅ Dataset is Ready

The uploaded data has been:

✔ Validated

✔ Cleaned

✔ Feature Engineered

✔ Prepared for AI Prediction

Click the button below to start Batch Prediction.
""")

predict = st.button(
    "🚀 Run Batch Prediction",
    use_container_width=True,
    type="primary"
)

st.divider()# ==========================================================
# BATCH PREDICTION ENGINE
# ==========================================================

if predict:

    try:

        # ---------------------------------------------
        # START TIMER
        # ---------------------------------------------

        start_time = time.time()

        st.markdown("## 🤖 AI Prediction Engine")

        status = st.empty()

        progress = st.progress(0)

        # ---------------------------------------------
        # STEP 1
        # ---------------------------------------------

        status.info("🔍 Validating Dataset...")

        progress.progress(10)

        time.sleep(0.4)

        # ---------------------------------------------
        # STEP 2
        # ---------------------------------------------

        status.info("🧹 Preparing Features...")

        progress.progress(30)

        time.sleep(0.4)

        # ---------------------------------------------
        # STEP 3
        # ---------------------------------------------

        status.info("⚙ Running CatBoost Model...")

        progress.progress(60)

        probabilities = model.predict_proba(upload_df)[:,1]

        predictions = model.predict(upload_df)

        time.sleep(0.4)

        # ---------------------------------------------
        # STEP 4
        # ---------------------------------------------

        status.info("📊 Generating Results...")

        progress.progress(90)

        results_df = upload_df.copy()

        results_df["DEFAULT_PROBABILITY"] = np.round(
            probabilities*100,
            2
        )

        results_df["PREDICTION"] = np.where(
            predictions==1,
            "Default",
            "Non Default"
        )

        # ---------------------------------------------
        # RISK LEVEL
        # ---------------------------------------------

        def classify_risk(prob):

            if prob < 30:

                return "Low Risk"

            elif prob < 60:

                return "Medium Risk"

            else:

                return "High Risk"

        results_df["RISK_LEVEL"] = results_df[
            "DEFAULT_PROBABILITY"
        ].apply(classify_risk)

        progress.progress(100)

        status.success(
            "✅ Batch Prediction Completed Successfully"
        )

        st.balloons()

        elapsed = time.time()-start_time

        st.divider()

        # ==================================================
        # EXECUTION SUMMARY
        # ==================================================

        total_records = len(results_df)

        total_default = (
            results_df["PREDICTION"]=="Default"
        ).sum()

        total_non_default = (
            results_df["PREDICTION"]=="Non Default"
        ).sum()

        avg_probability = results_df[
            "DEFAULT_PROBABILITY"
        ].mean()

        high_risk = (
            results_df["RISK_LEVEL"]=="High Risk"
        ).sum()

        medium_risk = (
            results_df["RISK_LEVEL"]=="Medium Risk"
        ).sum()

        low_risk = (
            results_df["RISK_LEVEL"]=="Low Risk"
        ).sum()

        st.markdown("## 📊 Batch Prediction Summary")

        k1,k2,k3,k4 = st.columns(4)

        with k1:

            st.metric(
                "Customers",
                f"{total_records:,}"
            )

        with k2:

            st.metric(
                "Predicted Default",
                f"{total_default:,}"
            )

        with k3:

            st.metric(
                "Predicted Safe",
                f"{total_non_default:,}"
            )

        with k4:

            st.metric(
                "Average Probability",
                f"{avg_probability:.2f}%"
            )

        st.divider()

        # ==================================================
        # PROCESSING STATISTICS
        # ==================================================

        st.markdown("## ⚡ Processing Statistics")

        s1,s2,s3,s4 = st.columns(4)

        with s1:

            st.metric(
                "Execution Time",
                f"{elapsed:.2f} sec"
            )

        with s2:

            st.metric(
                "Rows / Second",
                f"{(total_records/elapsed):.0f}"
            )

        with s3:

            st.metric(
                "Completed",
                datetime.now().strftime("%H:%M:%S")
            )

        with s4:

            st.metric(
                "Model",
                "CatBoost"
            )

        st.divider()

        # ==================================================
        # PORTFOLIO RISK
        # ==================================================

        st.markdown("## 🚨 Portfolio Risk Assessment")

        if high_risk > total_records*0.50:

            st.error(
                "🔴 HIGH PORTFOLIO RISK"
            )

        elif high_risk > total_records*0.25:

            st.warning(
                "🟡 MODERATE PORTFOLIO RISK"
            )

        else:

            st.success(
                "🟢 LOW PORTFOLIO RISK"
            )

        r1,r2,r3 = st.columns(3)

        with r1:

            st.metric(
                "High Risk",
                high_risk
            )

        with r2:

            st.metric(
                "Medium Risk",
                medium_risk
            )

        with r3:

            st.metric(
                "Low Risk",
                low_risk
            )

        st.divider()

        # ==================================================
        # RESULTS TABLE
        # ==================================================

        st.markdown("## 📋 Prediction Results")

        display_columns = []

        important_columns = [

            "AMT_INCOME_TOTAL",

            "AMT_CREDIT",

            "AGE_YEARS",

            "DEFAULT_PROBABILITY",

            "PREDICTION",

            "RISK_LEVEL"

        ]

        for col in important_columns:

            if col in results_df.columns:

                display_columns.append(col)

        st.dataframe(

            results_df[
                display_columns
            ],

            use_container_width=True,

            height=450

        )

        st.divider()
        # ==========================================================
        # PREDICTION ANALYTICS
        # ==========================================================

        st.markdown("## 📈 Prediction Analytics")

        chart1, chart2 = st.columns(2)

        with chart1:

            prediction_counts = (
                results_df["PREDICTION"]
                .value_counts()
                .reset_index()
            )

            prediction_counts.columns = [
                "Prediction",
                "Customers"
            ]

            fig = px.pie(
                prediction_counts,
                names="Prediction",
                values="Customers",
                hole=0.45,
                title="Prediction Distribution"
            )

            fig.update_layout(height=450)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with chart2:

            risk_counts = (
                results_df["RISK_LEVEL"]
                .value_counts()
                .reset_index()
            )

            risk_counts.columns = (
                "Risk Level",
                "Customers"
            )

            fig = px.bar(
                risk_counts,
                x="Risk Level",
                y="Customers",
                text="Customers",
                color="Risk Level",
                title="Risk Distribution"
            )

            fig.update_layout(
                height=450,
                xaxis_title="Risk Level",
                yaxis_title="Customers"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.divider()

        # ==========================================================
        # DEFAULT PROBABILITY DISTRIBUTION
        # ==========================================================

        st.markdown("## 📊 Default Probability Distribution")

        fig = px.histogram(
            results_df,
            x="DEFAULT_PROBABILITY",
            nbins=30,
            color="RISK_LEVEL",
            title="Probability Distribution"
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # ==========================================================
        # HIGH RISK CUSTOMERS
        # ==========================================================

        st.markdown("## 🚨 High Risk Customers")

        high_df = results_df[
            results_df["RISK_LEVEL"]=="High Risk"
        ]

        if len(high_df)>0:

            cols=[]

            for c in [
                "AMT_INCOME_TOTAL",
                "AMT_CREDIT",
                "AGE_YEARS",
                "DEFAULT_PROBABILITY",
                "RISK_LEVEL"
            ]:

                if c in high_df.columns:

                    cols.append(c)

            st.dataframe(
                high_df[cols],
                use_container_width=True,
                height=350
            )

        else:

            st.success(
                "No High Risk Customers Found."
            )

        st.divider()

        # ==========================================================
        # EXECUTIVE SUMMARY
        # ==========================================================

        st.markdown("## 📋 Executive Summary")

        left,right = st.columns(2)

        with left:

            st.success(f"""

### Batch Prediction Report

• Total Customers : **{total_records:,}**

• Default Predictions : **{total_default:,}**

• Safe Customers : **{total_non_default:,}**

• Average Probability : **{avg_probability:.2f}%**

• Execution Time : **{elapsed:.2f} sec**

""")

        with right:

            st.info(f"""

### Risk Portfolio

🟢 Low Risk : **{low_risk:,}**

🟡 Medium Risk : **{medium_risk:,}**

🔴 High Risk : **{high_risk:,}**

Prediction Date

**{datetime.now().strftime('%d-%m-%Y %H:%M')}**

""")

        st.divider()

        # ==========================================================
        # DOWNLOAD RESULTS
        # ==========================================================

        st.markdown("## 📥 Export Results")

        csv = results_df.to_csv(
            index=False
        ).encode("utf-8")

        download1,download2 = st.columns(2)

        with download1:

            st.download_button(
                "📄 Download CSV",
                csv,
                "batch_prediction_results.csv",
                "text/csv",
                use_container_width=True
            )

        with download2:

            excel = results_df.to_excel(
                "batch_prediction_results.xlsx",
                index=False
            )

            with open(
                "batch_prediction_results.xlsx",
                "rb"
            ) as f:

                st.download_button(
                    "📊 Download Excel",
                    f,
                    "batch_prediction_results.xlsx",
                    use_container_width=True
                )

        st.divider()

        # ==========================================================
        # MODEL INFORMATION
        # ==========================================================

        with st.expander("🤖 Model Information"):

            st.write("### AI Model")

            st.write("Model : CatBoost Classifier")

            st.write("Pipeline : Scikit-learn Pipeline")

            st.write("Prediction : Binary Classification")

            st.write(
                f"Input Features : {template.shape[1]}"
            )

            st.write(
                f"Records Processed : {total_records:,}"
            )

            st.write(
                f"Execution Time : {elapsed:.2f} sec"
            )

        st.divider()

        # ==========================================================
        # FOOTER
        # ==========================================================

        st.markdown(
        """
        <hr>

        <center>

        <h3>🏦 AI Financial Risk Analytics Platform</h3>

        Batch Prediction Module

        Developed using

        <b>Python • CatBoost • Streamlit • Plotly</b>

        </center>
        """,
        unsafe_allow_html=True
        )

    except Exception as e:

        st.error("❌ Batch Prediction Failed")

        st.exception(e)
