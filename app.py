import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Financial Risk Analytics",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:bold;
text-align:center;
color:white;
}

.sub-title{
font-size:22px;
text-align:center;
color:#CBD5E1;
}

.feature-card{
background-color:#1E293B;
padding:18px;
border-radius:12px;
border:1px solid #334155;
margin-bottom:15px;
color:white;
}

.feature-card h3{
color:white;
}

.feature-card ul{
padding-left:20px;
}

.feature-card li{
color:#E2E8F0;
margin-bottom:8px;
}

.footer{
text-align:center;
font-size:15px;
color:#94A3B8;
padding-top:25px;
}

</style>
""", unsafe_allow_html=True)
# =====================================================
# HEADER
# =====================================================

st.markdown(
"<div class='main-title'>🏦 AI Financial Risk Analytics Platform</div>",
unsafe_allow_html=True)

st.markdown(
"<div class='sub-title'>AI Powered Loan Default Prediction & Business Intelligence Platform</div>",
unsafe_allow_html=True)

st.divider()

# =====================================================
# QUICK NAVIGATION
# =====================================================

st.subheader("🚀 Modules")

c1,c2,c3,c4,c5=st.columns(5)

with c1:
    st.info("📊 Dashboard")

with c2:
    st.success("💳 Loan Prediction")

with c3:
    st.warning("📈 Analytics")

with c4:
    st.error("📂 Batch Prediction")

with c5:
    st.info("ℹ About")

st.divider()

# =====================================================
# PLATFORM OVERVIEW
# =====================================================

st.header("📌 Platform Overview")

st.write("""
This platform helps financial institutions analyze customer information,
estimate loan default probability using Machine Learning,
identify high-risk applicants,
and support lending decisions through interactive analytics dashboards.
""")

st.divider()

# =====================================================
# KPI SECTION
# =====================================================

st.header("📊 Project Statistics")

k1,k2,k3,k4=st.columns(4)

with k1:
    st.metric("Model","CatBoost")

with k2:
    st.metric("Features","109")

with k3:
    st.metric("Prediction","Binary")

with k4:
    st.metric("Deployment","Streamlit")

st.divider()

# =====================================================
# FEATURES
# =====================================================

st.header("🚀 Core Features")

col1,col2,col3=st.columns(3)

with col1:

    st.markdown("""
<div class="feature-card">

<h3>🤖 AI Prediction</h3>

<ul>
<li>Single Prediction</li>
<li>Batch Prediction</li>
<li>Risk Classification</li>
</ul>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>📊 Dashboard</h3>

<ul>
<li>KPIs</li>
<li>Interactive Charts</li>
<li>Filters</li>
</ul>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="feature-card">

<h3>📈 Analytics</h3>

<ul>
<li>Business Insights</li>
<li>Customer Analysis</li>
<li>Risk Distribution</li>
</ul>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>📂 Batch Processing</h3>

<ul>
<li>CSV Upload</li>
<li>Bulk Prediction</li>
<li>Download Results</li>
</ul>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="feature-card">

<h3>⚡ Machine Learning</h3>

<ul>
<li>Feature Engineering</li>
<li>CatBoost</li>
<li>Probability Prediction</li>
</ul>

</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="feature-card">

<h3>📉 Risk Analysis</h3>

<ul>
<li>Low Risk</li>
<li>Medium Risk</li>
<li>High Risk</li>
</ul>

</div>
""", unsafe_allow_html=True)

st.divider()

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.header("🛠 Technology Stack")

t1,t2,t3,t4=st.columns(4)

with t1:
    st.success("Python")

with t2:
    st.success("CatBoost")

with t3:
    st.success("Scikit-Learn")

with t4:
    st.success("Streamlit")

t5,t6,t7,t8=st.columns(4)

with t5:
    st.success("Pandas")

with t6:
    st.success("NumPy")

with t7:
    st.success("Plotly")

with t8:
    st.success("Joblib")

st.divider()

# =====================================================
# WORKFLOW
# =====================================================

st.header("⚙ AI Workflow")

st.markdown("""

Dataset

⬇

Data Cleaning

⬇

Feature Engineering

⬇

Model Training

⬇

Prediction

⬇

Risk Analytics

⬇

Business Intelligence

""")

st.divider()

# =====================================================
# PROJECT HIGHLIGHTS
# =====================================================

st.header("🏆 Project Highlights")

st.write("✔ AI-Powered Loan Default Prediction")

st.write("✔ Business Intelligence Dashboard")

st.write("✔ Advanced Customer Analytics")

st.write("✔ Batch Prediction")

st.write("✔ Downloadable Reports")

st.write("✔ Interactive Visualizations")

st.write("✔ Professional Portfolio Project")

st.divider()

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class="footer">

Developed using Python • Streamlit • CatBoost • Plotly

AI Financial Risk Analytics Platform © 2026

</div>
""",unsafe_allow_html=True)