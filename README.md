 🛍 E-Commerce Return Fraud Detection Dashboard

# 1) Why I Built This

E commerce companies faces many frauds or losses due to:

- Products get returned
- Fake return behaviour
- High-value item returns
- Cash-on-delivery(COD) misuse

So, I built a simple dashboard which shows or helps to identify risky customers.

---

# 2) Problem Statement

Currently:

- Fraud teams have to manually check the returned items
- There is no risk scoring system
- It's hard to understand which customer to investigate first

This creates:

- Time wastage
- Financial losses
- No fraud visibility

---

# 3) My Goal With This Project

To build a fraud risk ****dashboard that:

- Calculates risk score for customers
- Categories them according to their priority as:
1) Low risk
2) Medium/Moderate risk
3) High risk
- Show fraud exposure clearly

This is a rule-based MVP (Minimum Viable Product)

---

# 4) Who Would Use This

- Fraud analysts
- Risk team
- Finance team
- Product managers

---

# 5) Features I Built

- Risk score calculation
- Risk category
- Fraud percentage
- High risk percentage
- Fraud alert message
- Estimated fraud loss
- Top 5 risky customers
- Interactive chart
- Search by Customer-ID
- Filter risk category
- Download CSV report

---

# 6) Risk Scoring Logic

I created a simple scoring formula:

Risk Score = (Return Rate × 50)

- (High Value Returns × 3)
- (COD Orders × 1.5)

**Why?**

- Return rate is strongest fraud signal
- High value returns increase financial risk
- COD orders slightly increase risk

Score is capped between 0–100.

**Categories:**

- **Low Risk: < 30**
- **Medium Risk: 30–69**
- **High Risk: ≥ 70**

This is a rule-based system

---

# 7) KPIs I Defined

## Primary KPIs

### High Risk %

High Risk Customers / Total Customers

This tells us overall fraud exposure.

### Estimated Fraud Loss

High Risk Customers × ₹1000

This gives approximate financial impact.

### Risk Distribution

How many customers fall into:

- Low
- Medium
- High

This shows overall system health.

## Secondary KPIs

- Average return rate
- Frequency of high value returns
- Alert frequency

---

# 8) What Success Looks Like

This product is successful if:

- High risk % reduces over time
- Fraud loss decreases
- Investigation becomes faster
- Fraud team can prioritize easily

---

# 9) Limitations

- Uses synthetic data
- Rule-based scoring may not be that much perfect
- There's no historical tracking
- Real ML Model is not used

---

# 10) Tech Limitations

- Python
- Streamlit
- Pandas
- Data Visualization Libraries
- Synthetic Dataset

---

# 11) What I Learned Form This Project

- How to define and handle a problem
- How to think wrt / in terms of  KPIs
- How product decisions impact business
