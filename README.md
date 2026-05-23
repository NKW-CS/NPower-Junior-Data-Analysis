## Team Contributions
* **Nuha Warsi** (@NKW-CS) - Exploratory Data Analysis (EDA)
* **Divya Patel** (@pateldiya174-star/Selenium) - Exploratory Data Analysis (EDA)
* **Medhanit Melkie** (@ICode-Medi) - Data Cleaning & Data Wrangling
* **Edwin Palacios** (@elpalaciosc) - Data Cleaning & Data Wrangling
* **Froila** (@FroilaStephanie) - Dashboard & Visualization
* **Diane King 6** (@DKTODesigns) - Project Documentation & Presentation

* **My Part** *
🛠️ Data Science & Machine Learning Pipeline

## 🛠️ My Contributions: Data Science & Machine Learning Pipeline
*Section authored by Nuha Warsi (@NKW-CS)*

### 1. Descriptive Analytics & Outlier Identification
* **Statistical Profiling:** Conducted thorough summary statistics using `df.describe()` on key financial features including `income`, `loan_amount`, `credit_score`, `property_value`, and `ltv`.
* **Outlier & Anomaly Detection:** Identified massive skewness and anomalies in the dataset—specifically noting extreme max outliers in borrower `income` ($578,580) and an unrealistic maximum `ltv` (Loan-to-Value) ratio of 7,831.25%.

### 2. Exploratory Data Analysis (EDA) & Segmentation
* **Risk Class Distributions:** Evaluated the portfolio's baseline default rate, establishing that 24.50% of the observations represent defaults (`status = 1`).
* **Categorical Segmentation:** Aggregated and compared average loan volumes across loan programs, identifying that Type 1 (Conventional) and Type 3 (VA) loans carry significantly higher average amounts (*$340k+) compared to Type 2 (FHA) loans (*$258k).
* **Correlation Analysis:** Measured linear relationships against borrower income, discovering moderate positive correlations with `loan_amount` (0.44) and `property_value` (0.39), alongside a negative correlation with debt-to-income ratios (`dtir1` at -0.25).
* **Advanced Regressions & Data Visualization:** Built tailored Seaborn (`sns.regplot`) and Matplotlib visuals, including default rates by loan purpose, box plots isolating debt-to-income spreads, and regression lines mapping `property_value` vs. `loan_amount` and `income` vs. `loan_amount`.

### 3. Predictive Modeling & Model Testing
Developed and evaluated multi-variable regression models to predict `loan_amount` based on a feature subset of `['income', 'credit_score', 'status', 'rate_of_interest', 'ltv', 'dtir1']`.
* **Baseline Linear Regression:** Achieved an initial baseline $R^2$ score of **0.2296**.
* **Feature Engineering Pipeline:** Engineered a Scikit-Learn Pipeline combining `StandardScaler` and 2nd-degree `PolynomialFeatures` with a Linear Regression estimator, successfully boosting model explanation capacity to an $R^2$ of **0.3532**.
* **Train-Test Validation with Regularization:** Split the dataset using an 85/15 train-test split (122,385 training rows / 21,598 testing rows). Evaluated regularized models against the test set:
  * **Linear Ridge Regression ($\alpha=0.1$):** Test $R^2$ of **0.2265**
  * **Polynomial Ridge Regression (Degree 2, $\alpha=0.1$):** Test $R^2$ of **0.3284**


# Loan Default Risk Analysis Dashboard

## Project Overview

This project focuses on analyzing loan default data to identify patterns, trends, and potential financial risk indicators within a lending portfolio.

Using Python and data analytics techniques, the dataset was cleaned, transformed, and explored through statistical analysis and visualization. The project aims to better understand borrower behavior and factors that may contribute to loan default risk.

The analysis includes:

- Data cleaning and preparation
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Data visualization
- Predictive modeling
- Interactive dashboard development

Key areas explored throughout the project include:

- Regional loan default patterns
- Credit score distribution
- Loan amount trends
- Borrower financial indicators
- Relationships between lending variables and default risk

Several visualizations and machine learning models were developed to support business intelligence insights and demonstrate how data analytics can assist financial institutions in making more informed lending decisions.

The final stage of the project includes an interactive dashboard built with Dash and Plotly to allow dynamic exploration of loan default trends and borrower risk factors.

---

# Dashboard Overview

## Interactive Loan Default Risk Dashboard

Features included in the dashboard:

- Dynamic filtering by:
  - Region
  - Month
  - Loan Type
  - Loan Status

- KPI cards displaying:
  - Total Applications
  - Average Credit Score
  - Average Interest Rate
  - Default Rate

- Interactive visualizations including:
  - Default Rate by Region
  - Default Rate by Loan Type
  - Loan Type Distribution
  - Credit Score Distribution
  - Heatmaps
  - Monthly Loan Volume Trends

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Dash
- Scikit-learn
- Jupyter Notebook
- Visual Studio Code

---

# Project Structure

```text
loan-default-risk-analysis-dashboard/
│
├── app.py
├── Data_Analytics_Project_Activity.ipynb
├── Loan_Default.csv
├── requirements.txt
├── README.md
│
├── visuals/
│   ├── dashboard-overview.png
│   ├── dashboard-visualizations.png
│   ├── monthly-loan-volume-2019.png
│   ├── loan-purpose-default-rate.png
│   ├── loan-type-distribution.png
│   ├── outlier-analysis.png
│   └── additional visualizations...
│
└── presentation/
    └── Loan_Default_Risk_Analysis_Presentation.pdf
