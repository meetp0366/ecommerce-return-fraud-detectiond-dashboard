import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Title
st.title("E-commerce Return Fraud Risk Dashboard")
st.write("This dashboard identifies high-risk customers based on return behavior.")

# Set random seed
np.random.seed(42)

# Number of customers
n = 500

# Create dataset properly (REALISTIC LOGIC)
data = pd.DataFrame({
    "Customer_ID": range(1, n+1),
    "Total_Orders": np.random.randint(1, 50, n)
})

# Ensure realistic relationships
data["Total_Returns"] = data["Total_Orders"].apply(
    lambda x: np.random.randint(0, x+1)
)

data["COD_Orders"] = data["Total_Orders"].apply(
    lambda x: np.random.randint(0, x+1)
)

data["High_Value_Returns"] = data["Total_Returns"].apply(
    lambda x: np.random.randint(0, x+1)
)

# Reorder columns
data = data[[
    "Customer_ID",
    "Total_Orders",
    "Total_Returns",
    "High_Value_Returns",
    "COD_Orders"
]]

# Calculate Return Rate
data["Return_Rate"] = data["Total_Returns"] / data["Total_Orders"]

# Calculate Fraud Risk Score
data["Risk_Score"] = (
    data["Return_Rate"] * 50 +
    data["High_Value_Returns"] * 3 +
    data["COD_Orders"] * 1.5
)

# Keep Risk Score between 0 and 100
data["Risk_Score"] = np.clip(data["Risk_Score"], 0, 100)

# Categorize Risk
def categorize(score):
    if score < 30:
        return "Low Risk"
    elif score < 70:
        return "Medium Risk"
    else:
        return "High Risk"

data["Risk_Category"] = data["Risk_Score"].apply(categorize)

# ============================
# Dashboard UI
# ============================

st.subheader("📊 Fraud Risk Overview")

total_customers = len(data)
high_risk_count = len(data[data["Risk_Category"] == "High Risk"])
fraud_percentage = round((high_risk_count / total_customers) * 100, 2)

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", total_customers)
col2.metric("High Risk Customers", high_risk_count)
col3.metric("High Risk %", f"{fraud_percentage}%")

# Fraud Alert
if fraud_percentage > 40:
    st.error("⚠️ High Fraud Risk Detected! Immediate review recommended.")
elif fraud_percentage > 20:
    st.warning("⚠️ Moderate Fraud Risk. Monitor closely.")
else:
    st.success("✅ Fraud Risk is Under Control.")

# Estimated Fraud Loss
estimated_loss_per_customer = 1000
total_estimated_loss = high_risk_count * estimated_loss_per_customer

st.subheader("💰 Estimated Fraud Impact")
st.metric("Estimated Monthly Fraud Loss (₹)", total_estimated_loss)

# Top 5 High Risk Customers
st.subheader("🚨 Top 5 High Risk Customers")
top_risky = data.sort_values(by="Risk_Score", ascending=False).head(5)
st.dataframe(top_risky)

# Risk Distribution Chart
st.subheader("📊 Risk Category Distribution")

risk_counts = data["Risk_Category"].value_counts().reset_index()
risk_counts.columns = ["Risk Category", "Count"]

fig = px.bar(
    risk_counts,
    x="Risk Category",
    y="Count",
    color="Risk Category",
    text="Count",
    color_discrete_map={
    "High Risk": "#d16d6d",
    "Medium Risk": "#e0c97a",
    "Low Risk": "#7bc67b"
},    
)

fig.update_layout(
    plot_bgcolor="#0e1117",
    paper_bgcolor="#0e1117",
    font_color="white",
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("🔎 Search Customer by ID")

search_id = st.number_input(
    "Enter Customer ID",
    min_value=1,
    max_value=n,
    step=1
)

customer_data = data[data["Customer_ID"] == search_id]

if not customer_data.empty:
    st.dataframe(customer_data)

# Filter Section
st.subheader("🔍 Filter Customers")

selected_category = st.selectbox(
    "Select Risk Category",
    ["All", "Low Risk", "Medium Risk", "High Risk"]
)

if selected_category != "All":
    filtered_data = data[data["Risk_Category"] == selected_category]
else:
    filtered_data = data

def highlight_risk(row):
    if row["Risk_Category"] == "High Risk":
        return ["background-color: rgba(255, 99, 132, 0.15); color: #ff6b81; font-weight: 500"] * len(row)
    elif row["Risk_Category"] == "Medium Risk":
        return ["background-color: rgba(255, 193, 7, 0.15); color: #f4b400; font-weight: 500"] * len(row)
    else:
        return ["background-color: rgba(40, 167, 69, 0.15); color: #2ecc71; font-weight: 500"] * len(row)


styled_data = filtered_data.head(10).style.apply(highlight_risk, axis=1)
st.dataframe(styled_data)
# Convert filtered data to CSV
csv = filtered_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Data as CSV",
    data=csv,
    file_name="fraud_filtered_customers.csv",
    mime="text/csv",
)
