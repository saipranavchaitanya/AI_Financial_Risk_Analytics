import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import joblib
from pathlib import Path

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    return pd.read_csv(
        "data/train_data_engineered.csv"
    )

df = load_data()

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    return joblib.load(
        "models/best_model.pkl"
    )

model = load_model()

# ==========================================================
# HEADER
# ==========================================================

st.title("📈 AI Financial Risk Analytics")

st.write(
    "Advanced analytics and business intelligence for the loan portfolio."
)

st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("Analytics Filters")

gender = st.sidebar.multiselect(
    "Gender",
    sorted(df["CODE_GENDER"].unique()),
    default=sorted(df["CODE_GENDER"].unique())
)

education = st.sidebar.multiselect(
    "Education",
    sorted(df["NAME_EDUCATION_TYPE"].unique()),
    default=sorted(df["NAME_EDUCATION_TYPE"].unique())
)

filtered_df = df[
    (df["CODE_GENDER"].isin(gender))
    &
    (df["NAME_EDUCATION_TYPE"].isin(education))
]

st.success(
    f"{len(filtered_df):,} Customers Selected"
)
# ==========================================================
# EXECUTIVE KPI CALCULATIONS
# ==========================================================

total_customers = len(filtered_df)

default_rate = filtered_df["TARGET"].mean() * 100

avg_income = filtered_df["AMT_INCOME_TOTAL"].mean()

avg_credit = filtered_df["AMT_CREDIT"].mean()

avg_annuity = filtered_df["AMT_ANNUITY"].mean()

avg_age = filtered_df["AGE_YEARS"].mean()

avg_employment = filtered_df["EMPLOYMENT_YEARS"].mean()

avg_ext1 = filtered_df["EXT_SOURCE_1"].mean()

avg_ext2 = filtered_df["EXT_SOURCE_2"].mean()

avg_ext3 = filtered_df["EXT_SOURCE_3"].mean()

# ==========================================================
# EXECUTIVE DASHBOARD
# ==========================================================

st.markdown("## 📊 Executive Overview")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:

    st.metric(
        "👥 Customers",
        f"{total_customers:,}"
    )

with kpi2:

    st.metric(
        "⚠ Default Rate",
        f"{default_rate:.2f}%"
    )

with kpi3:

    st.metric(
        "💰 Avg Income",
        f"₹ {avg_income:,.0f}"
    )

with kpi4:

    st.metric(
        "🏦 Avg Credit",
        f"₹ {avg_credit:,.0f}"
    )

st.write("")

kpi5, kpi6, kpi7, kpi8 = st.columns(4)

with kpi5:

    st.metric(
        "💳 Avg Annuity",
        f"₹ {avg_annuity:,.0f}"
    )

with kpi6:

    st.metric(
        "🎂 Avg Age",
        f"{avg_age:.1f} Years"
    )

with kpi7:

    st.metric(
        "💼 Avg Employment",
        f"{avg_employment:.1f} Years"
    )

with kpi8:

    st.metric(
        "⭐ Avg External Score",
        f"{((avg_ext1 + avg_ext2 + avg_ext3) / 3):.3f}"
    )

st.divider()

# ==========================================================
# PORTFOLIO SUMMARY
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("📌 Portfolio Summary")

    st.write(f"**Total Customers:** {total_customers:,}")

    st.write(f"**Average Income:** ₹ {avg_income:,.0f}")

    st.write(f"**Average Credit:** ₹ {avg_credit:,.0f}")

    st.write(f"**Average Loan Annuity:** ₹ {avg_annuity:,.0f}")

    st.write(f"**Average Age:** {avg_age:.1f} Years")

    st.write(f"**Average Employment:** {avg_employment:.1f} Years")

with right:

    st.subheader("🚦Portfolio Risk")

    if default_rate < 10:

        st.success("🟢 Low Risk Portfolio")

    elif default_rate < 20:

        st.warning("🟡 Moderate Risk Portfolio")

    else:

        st.error("🔴 High Risk Portfolio")

    st.write(f"Default Rate : **{default_rate:.2f}%**")

    st.progress(min(default_rate / 100, 1.0))

st.divider()

# ==========================================================
# EXTERNAL SCORE ANALYSIS
# ==========================================================

st.markdown("## ⭐ External Credit Score Analysis")

score1, score2, score3 = st.columns(3)

with score1:

    st.metric(
        "External Score 1",
        f"{avg_ext1:.3f}"
    )

with score2:

    st.metric(
        "External Score 2",
        f"{avg_ext2:.3f}"
    )

with score3:

    st.metric(
        "External Score 3",
        f"{avg_ext3:.3f}"
    )

st.divider()
# ==========================================================
# ANALYTICS VISUALIZATIONS
# ==========================================================

st.markdown("## 📊 Business Analytics")

# ==========================================================
# ROW 1
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("Default Rate by Education")

    education_default = (
        filtered_df
        .groupby("NAME_EDUCATION_TYPE")["TARGET"]
        .mean()
        .reset_index()
    )

    education_default["TARGET"] *= 100

    fig = px.bar(
        education_default,
        x="NAME_EDUCATION_TYPE",
        y="TARGET",
        text="TARGET",
        title="Default Rate by Education"
    )

    fig.update_traces(texttemplate="%{text:.2f}%")

    fig.update_layout(
        height=450,
        xaxis_title="Education",
        yaxis_title="Default Rate (%)"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.subheader("Default Rate by Gender")

    gender_default = (
        filtered_df
        .groupby("CODE_GENDER")["TARGET"]
        .mean()
        .reset_index()
    )

    gender_default["TARGET"] *= 100

    fig = px.bar(
        gender_default,
        x="CODE_GENDER",
        y="TARGET",
        text="TARGET",
        title="Default Rate by Gender"
    )

    fig.update_traces(texttemplate="%{text:.2f}%")

    fig.update_layout(
        height=450,
        xaxis_title="Gender",
        yaxis_title="Default Rate (%)"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# ROW 2
# ==========================================================

col3, col4 = st.columns(2)

with col3:

    st.subheader("Income by Education")

    income_education = (
        filtered_df
        .groupby("NAME_EDUCATION_TYPE")["AMT_INCOME_TOTAL"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        income_education,
        x="NAME_EDUCATION_TYPE",
        y="AMT_INCOME_TOTAL",
        text="AMT_INCOME_TOTAL",
        title="Average Income"
    )

    fig.update_traces(texttemplate="₹ %{text:,.0f}")

    fig.update_layout(
        height=450,
        xaxis_title="Education",
        yaxis_title="Income"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    st.subheader("Credit by Income Type")

    credit_income = (
        filtered_df
        .groupby("NAME_INCOME_TYPE")["AMT_CREDIT"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        credit_income,
        x="NAME_INCOME_TYPE",
        y="AMT_CREDIT",
        text="AMT_CREDIT",
        title="Average Credit"
    )

    fig.update_traces(texttemplate="₹ %{text:,.0f}")

    fig.update_layout(
        height=450,
        xaxis_title="Income Type",
        yaxis_title="Credit Amount"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# ROW 3
# ==========================================================

col5, col6 = st.columns(2)

with col5:

    st.subheader("External Credit Score Distribution")

    fig = px.histogram(
        filtered_df,
        x="EXT_SOURCE_2",
        nbins=30,
        title="External Score Distribution"
    )

    fig.update_layout(
        height=450,
        xaxis_title="External Score",
        yaxis_title="Customers"
    )

    st.plotly_chart(fig, use_container_width=True)

with col6:

    st.subheader("Loan Amount Distribution")

    fig = px.histogram(
        filtered_df,
        x="AMT_CREDIT",
        nbins=35,
        title="Loan Amount Distribution"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Loan Amount",
        yaxis_title="Customers"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# RISK SEGMENTATION
# ==========================================================

st.markdown("## 🎯 Customer Risk Segmentation")

risk_df = filtered_df.copy()

risk_df["Risk Segment"] = pd.cut(
    risk_df["EXT_SOURCE_2"],
    bins=[-1, 0.30, 0.60, 1],
    labels=[
        "High Risk",
        "Medium Risk",
        "Low Risk"
    ]
)

risk_counts = (
    risk_df["Risk Segment"]
    .value_counts()
    .reset_index()
)

risk_counts.columns = [
    "Risk Segment",
    "Customers"
]

fig = px.pie(
    risk_counts,
    names="Risk Segment",
    values="Customers",
    hole=0.45,
    title="Customer Risk Segmentation"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()
# ==========================================================
# CORRELATION ANALYSIS
# ==========================================================

st.markdown("## 🔥 Correlation Analysis")

numeric_columns = [
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "AMT_GOODS_PRICE",
    "AGE_YEARS",
    "EMPLOYMENT_YEARS",
    "EXT_SOURCE_1",
    "EXT_SOURCE_2",
    "EXT_SOURCE_3",
    "TARGET"
]

available_numeric = [
    col for col in numeric_columns
    if col in filtered_df.columns
]

corr = filtered_df[available_numeric].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    title="Correlation Heatmap"
)

fig.update_layout(height=650)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# FEATURE IMPORTANCE
# ==========================================================

st.markdown("## 🤖 Model Feature Importance")

try:

    estimator = model.named_steps.get("model", None)

    if estimator is None:
        estimator = model.steps[-1][1]

    if hasattr(estimator, "feature_importances_"):

        feature_names = model.named_steps["preprocessor"].get_feature_names_out()

        importance_df = pd.DataFrame({

            "Feature": feature_names,
            "Importance": estimator.feature_importances_

        })

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        ).head(20)

        fig = px.bar(
            importance_df,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top 20 Important Features"
        )

        fig.update_layout(height=700)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "Feature importance is not available for the current pipeline."
        )

except Exception as e:

    st.warning(
        f"Unable to display feature importance.\n\n{e}"
    )

st.divider()

# ==========================================================
# TOP RISK CUSTOMERS
# ==========================================================

st.markdown("## 🚨 High Risk Customer Groups")

top_risk = filtered_df.sort_values(
    by="AMT_CREDIT",
    ascending=False
).head(15)

columns = [
    "AMT_CREDIT",
    "AMT_INCOME_TOTAL",
    "AGE_YEARS",
    "EMPLOYMENT_YEARS",
    "NAME_EDUCATION_TYPE",
    "TARGET"
]

columns = [c for c in columns if c in top_risk.columns]

st.dataframe(
    top_risk[columns],
    use_container_width=True
)

st.divider()

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

st.markdown("## 💡 Executive Insights")

highest_default = (
    filtered_df
    .groupby("NAME_EDUCATION_TYPE")["TARGET"]
    .mean()
    .idxmax()
)

highest_income = (
    filtered_df["AMT_INCOME_TOTAL"]
    .max()
)

highest_credit = (
    filtered_df["AMT_CREDIT"]
    .max()
)

lowest_age = (
    filtered_df["AGE_YEARS"]
    .min()
)

highest_age = (
    filtered_df["AGE_YEARS"]
    .max()
)

left, right = st.columns(2)

with left:

    st.success(f"""

### Portfolio Highlights

• Total Customers : {total_customers:,}

• Average Income : ₹ {avg_income:,.0f}

• Average Credit : ₹ {avg_credit:,.0f}

• Highest Income : ₹ {highest_income:,.0f}

• Highest Credit : ₹ {highest_credit:,.0f}

""")

with right:

    st.info(f"""

### Customer Insights

• Highest Default Education :

**{highest_default}**

• Youngest Customer :

**{lowest_age:.0f} Years**

• Oldest Customer :

**{highest_age:.0f} Years**

""")

st.divider()

# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

st.markdown("## 📌 Business Recommendations")

if default_rate < 10:

    st.success("""
✅ Portfolio quality is excellent.

Recommended actions:

- Increase loan approvals

- Expand lending

- Maintain current credit policy

- Continue monitoring
""")

elif default_rate < 20:

    st.warning("""
⚠ Moderate portfolio risk.

Recommended actions:

- Improve customer verification

- Review medium-risk customers

- Monitor repayment behaviour

- Strengthen credit scoring
""")

else:

    st.error("""
🚨 High portfolio risk.

Recommended actions:

- Tighten approval policy

- Reduce exposure

- Increase fraud monitoring

- Manual verification required
""")

st.divider()

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

st.markdown("## 📥 Download Analytics Report")

analytics_report = filtered_df.describe(include="all")

csv = analytics_report.to_csv().encode("utf-8")

st.download_button(

    "⬇ Download Analytics Summary",

    data=csv,

    file_name="analytics_summary.csv",

    mime="text/csv"

)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
<center>

### 📈 AI Financial Risk Analytics Platform

Advanced Analytics Module

Powered by

Python • Streamlit • Plotly • CatBoost • Scikit-Learn

</center>
""",
unsafe_allow_html=True
)