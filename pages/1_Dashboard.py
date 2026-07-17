import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Financial Risk Dashboard",
    page_icon="📊",
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
    color:#1565C0;
}

.sub-title{
    font-size:18px;
    color:#616161;
}

.kpi{
    background:#F8F9FA;
    padding:15px;
    border-radius:12px;
    border:1px solid #E0E0E0;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    file_path = Path("data/dashboard_data.csv")

    df = pd.read_csv(file_path)

    return df

df = load_data()

# ==========================================================
# HEADER
# ==========================================================

st.markdown(
'<p class="main-title">📊 AI Financial Risk Analytics Dashboard</p>',
unsafe_allow_html=True
)

st.markdown(
'<p class="sub-title">Interactive Banking Risk Analytics Dashboard</p>',
unsafe_allow_html=True
)

st.divider()

# ==========================================================
# SIDEBAR FILTERS
# ==========================================================

st.sidebar.title("Dashboard Filters")

gender = st.sidebar.multiselect(
    "Gender",
    sorted(df["CODE_GENDER"].dropna().unique()),
    default=sorted(df["CODE_GENDER"].dropna().unique())
)

education = st.sidebar.multiselect(
    "Education",
    sorted(df["NAME_EDUCATION_TYPE"].dropna().unique()),
    default=sorted(df["NAME_EDUCATION_TYPE"].dropna().unique())
)

family = st.sidebar.multiselect(
    "Family Status",
    sorted(df["NAME_FAMILY_STATUS"].dropna().unique()),
    default=sorted(df["NAME_FAMILY_STATUS"].dropna().unique())
)

income_type = st.sidebar.multiselect(
    "Income Type",
    sorted(df["NAME_INCOME_TYPE"].dropna().unique()),
    default=sorted(df["NAME_INCOME_TYPE"].dropna().unique())
)

housing = st.sidebar.multiselect(
    "Housing Type",
    sorted(df["NAME_HOUSING_TYPE"].dropna().unique()),
    default=sorted(df["NAME_HOUSING_TYPE"].dropna().unique())
)

# ==========================================================
# APPLY FILTERS
# ==========================================================

filtered_df = df[
    (df["CODE_GENDER"].isin(gender)) &
    (df["NAME_EDUCATION_TYPE"].isin(education)) &
    (df["NAME_FAMILY_STATUS"].isin(family)) &
    (df["NAME_INCOME_TYPE"].isin(income_type)) &
    (df["NAME_HOUSING_TYPE"].isin(housing))
]

st.success(f"Showing {len(filtered_df):,} Customers")
# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_customers = len(filtered_df)

avg_income = filtered_df["AMT_INCOME_TOTAL"].mean()

avg_credit = filtered_df["AMT_CREDIT"].mean()

avg_annuity = filtered_df["AMT_ANNUITY"].mean()

avg_goods = filtered_df["AMT_GOODS_PRICE"].mean()

default_rate = filtered_df["TARGET"].mean() * 100

avg_age = filtered_df["AGE_YEARS"].mean()

avg_employment = filtered_df["EMPLOYMENT_YEARS"].mean()

# ==========================================================
# KPI CARDS
# ==========================================================

st.markdown("## 📈 Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:

    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

with kpi2:

    st.metric(
        "💰 Avg Income",
        f"₹ {avg_income:,.0f}"
    )

with kpi3:

    st.metric(
        "🏦 Avg Credit",
        f"₹ {avg_credit:,.0f}"
    )

with kpi4:

    st.metric(
        "💳 Avg Annuity",
        f"₹ {avg_annuity:,.0f}"
    )

st.write("")

kpi5, kpi6, kpi7, kpi8 = st.columns(4)

with kpi5:

    st.metric(
        "🏠 Avg Goods Price",
        f"₹ {avg_goods:,.0f}"
    )

with kpi6:

    st.metric(
        "⚠ Default Rate",
        f"{default_rate:.2f}%"
    )

with kpi7:

    st.metric(
        "🎂 Avg Age",
        f"{avg_age:.1f} Years"
    )

with kpi8:

    st.metric(
        "💼 Avg Employment",
        f"{avg_employment:.1f} Years"
    )

st.divider()

# ==========================================================
# QUICK INSIGHTS
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("📌 Dataset Summary")

    st.write(f"Total Records : **{total_customers:,}**")

    st.write(f"Average Income : **₹ {avg_income:,.0f}**")

    st.write(f"Average Credit : **₹ {avg_credit:,.0f}**")

    st.write(f"Average Age : **{avg_age:.1f} Years**")

with right:

    st.subheader("⚡ Portfolio Health")

    if default_rate < 10:

        st.success("Very Low Credit Risk Portfolio")

    elif default_rate < 20:

        st.warning("Moderate Credit Risk Portfolio")

    else:

        st.error("High Credit Risk Portfolio")

    st.write(f"Default Rate : **{default_rate:.2f}%**")

st.divider()
# ==========================================================
# VISUAL ANALYTICS
# ==========================================================

st.markdown("## 📊 Visual Analytics Dashboard")

# ==========================================================
# ROW 1
# ==========================================================

chart1, chart2 = st.columns(2)

with chart1:

    st.subheader("Default Distribution")

    default_counts = (
        filtered_df["TARGET"]
        .map({0: "Non Default", 1: "Default"})
        .value_counts()
        .reset_index()
    )

    default_counts.columns = ["Status", "Customers"]

    fig = px.pie(
        default_counts,
        names="Status",
        values="Customers",
        hole=0.45,
        title="Loan Default Distribution"
    )

    fig.update_layout(height=450)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with chart2:

    st.subheader("Education Distribution")

    education_df = (
        filtered_df["NAME_EDUCATION_TYPE"]
        .value_counts()
        .reset_index()
    )

    education_df.columns = [
        "Education",
        "Customers"
    ]

    fig = px.bar(
        education_df,
        x="Education",
        y="Customers",
        title="Education Level",
        text="Customers"
    )

    fig.update_layout(
        xaxis_title="Education",
        yaxis_title="Customers",
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# ROW 2
# ==========================================================

chart3, chart4 = st.columns(2)

with chart3:

    st.subheader("Income Distribution")

    fig = px.histogram(
        filtered_df,
        x="AMT_INCOME_TOTAL",
        nbins=40,
        title="Income Distribution"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Income",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with chart4:

    st.subheader("Credit Distribution")

    fig = px.histogram(
        filtered_df,
        x="AMT_CREDIT",
        nbins=40,
        title="Credit Amount Distribution"
    )

    fig.update_layout(
        height=450,
        xaxis_title="Credit Amount",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# ROW 3
# ==========================================================

chart5, chart6 = st.columns(2)

with chart5:

    st.subheader("Income vs Credit")

    sample_df = filtered_df.sample(
        min(5000, len(filtered_df)),
        random_state=42
    )

    fig = px.scatter(
        sample_df,
        x="AMT_INCOME_TOTAL",
        y="AMT_CREDIT",
        color="TARGET",
        title="Income vs Credit",
        opacity=0.7
    )

    fig.update_layout(height=500)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with chart6:

    st.subheader("Age Distribution")

    fig = px.histogram(
        filtered_df,
        x="AGE_YEARS",
        nbins=30,
        title="Customer Age Distribution"
    )

    fig.update_layout(
        height=500,
        xaxis_title="Age",
        yaxis_title="Customers"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

# ==========================================================
# ROW 4
# ==========================================================

chart7, chart8 = st.columns(2)

with chart7:

    st.subheader("Employment Years")

    fig = px.histogram(
        filtered_df,
        x="EMPLOYMENT_YEARS",
        nbins=30,
        title="Employment Experience"
    )

    fig.update_layout(
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with chart8:

    st.subheader("Family Status")

    family_df = (
        filtered_df["NAME_FAMILY_STATUS"]
        .value_counts()
        .reset_index()
    )

    family_df.columns = [
        "Family Status",
        "Customers"
    ]

    fig = px.bar(
        family_df,
        x="Family Status",
        y="Customers",
        text="Customers",
        title="Family Status Distribution"
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
# BUSINESS INSIGHTS
# ==========================================================

st.markdown("## 💡 Business Insights")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏆 Top 10 Highest Income Customers")

    top_income = (
        filtered_df[
            [
                "AMT_INCOME_TOTAL",
                "AMT_CREDIT",
                "AGE_YEARS",
                "NAME_EDUCATION_TYPE",
                "NAME_FAMILY_STATUS"
            ]
        ]
        .sort_values(
            by="AMT_INCOME_TOTAL",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_income,
        use_container_width=True
    )

with col2:

    st.subheader("🏦 Top 10 Highest Credit Customers")

    top_credit = (
        filtered_df[
            [
                "AMT_CREDIT",
                "AMT_INCOME_TOTAL",
                "AGE_YEARS",
                "NAME_EDUCATION_TYPE",
                "TARGET"
            ]
        ]
        .sort_values(
            by="AMT_CREDIT",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        top_credit,
        use_container_width=True
    )

st.divider()

# ==========================================================
# RISK ANALYSIS
# ==========================================================

st.markdown("## ⚠ Risk Analysis")

risk1, risk2, risk3 = st.columns(3)

with risk1:

    high_credit = (
        filtered_df["AMT_CREDIT"] > filtered_df["AMT_CREDIT"].median()
    ).sum()

    st.metric(
        "High Credit Customers",
        f"{high_credit:,}"
    )

with risk2:

    high_income = (
        filtered_df["AMT_INCOME_TOTAL"] >
        filtered_df["AMT_INCOME_TOTAL"].median()
    ).sum()

    st.metric(
        "High Income Customers",
        f"{high_income:,}"
    )

with risk3:

    defaults = (
        filtered_df["TARGET"] == 1
    ).sum()

    st.metric(
        "Loan Defaults",
        f"{defaults:,}"
    )

st.divider()

# ==========================================================
# CUSTOMER DATA
# ==========================================================

st.markdown("## 📋 Customer Dataset")

display_columns = [
    "CODE_GENDER",
    "AGE_YEARS",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY",
    "EMPLOYMENT_YEARS",
    "NAME_EDUCATION_TYPE",
    "NAME_FAMILY_STATUS",
    "TARGET"
]

available_columns = [
    col for col in display_columns
    if col in filtered_df.columns
]

st.dataframe(
    filtered_df[available_columns],
    use_container_width=True,
    height=450
)

st.divider()

# ==========================================================
# DOWNLOAD FILTERED DATA
# ==========================================================

st.markdown("## 📥 Export Dashboard Data")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Filtered Dataset",
    data=csv,
    file_name="filtered_dashboard_data.csv",
    mime="text/csv"
)

st.divider()

# ==========================================================
# MODEL INFORMATION
# ==========================================================

with st.expander("🤖 Model Information", expanded=False):

    info1, info2 = st.columns(2)

    with info1:

        st.markdown("### Project")

        st.write("**Project:** AI Financial Risk Analytics")

        st.write("**Model:** CatBoost Classifier")

        st.write("**Problem:** Loan Default Prediction")

        st.write("**Task:** Binary Classification")

    with info2:

        st.markdown("### Dataset")

        st.write(f"**Total Records:** {len(df):,}")

        st.write(f"**Filtered Records:** {len(filtered_df):,}")

        st.write(f"**Features:** {df.shape[1]}")

        st.write("**Source:** Home Credit Default Risk")

st.divider()

# ==========================================================
# KEY INSIGHTS
# ==========================================================

st.markdown("## 📌 Dashboard Insights")

insight1, insight2 = st.columns(2)

with insight1:

    st.success(
        f"""
### Portfolio Summary

- Total Customers : {total_customers:,}
- Average Income : ₹ {avg_income:,.0f}
- Average Credit : ₹ {avg_credit:,.0f}
- Default Rate : {default_rate:.2f}%
"""
    )

with insight2:

    if default_rate < 10:

        st.success(
            """
### Risk Assessment

✅ Excellent Portfolio

The overall default rate is low.
Current lending portfolio appears healthy.
"""
        )

    elif default_rate < 20:

        st.warning(
            """
### Risk Assessment

⚠ Moderate Risk

Portfolio requires periodic monitoring.
"""
        )

    else:

        st.error(
            """
### Risk Assessment

🚨 High Risk

Default rate is high.
Loan approval policies should be reviewed.
"""
        )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
"""
<center>

### 🏦 AI Financial Risk Analytics Platform

Developed using **Python**, **Streamlit**, **CatBoost**, **Scikit-Learn**, **Pandas**, and **Plotly**.

</center>
""",
unsafe_allow_html=True
)