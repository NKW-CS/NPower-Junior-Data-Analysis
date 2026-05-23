## Team Contributions
* **Nuha Warsi** (@NKW-CS) - Exploratory Data Analysis (EDA)
* **Divya Patel** (@pateldiya174-star/Selenium) - Exploratory Data Analysis (EDA)
* **Medhanit Melkie** (@ICode-Medi) - Data Cleaning & Data Wrangling
* **Edwin Palacios** (@elpalaciosc) - Data Cleaning & Data Wrangling
* **Froila** (@FroilaStephanie) - Dashboard & Visualization
* **Diane King 6** (@DKTODesigns) - Project Documentation & Presentation

* **My Part** *
* 🛠️ Data Science & Machine Learning Pipeline

### 1. Data Cleaning & Preprocessing
* **Outlier Detection & Handling:** Identified anomalies in financial indicators (like extreme loan amounts or credit scores) using statistical methods and handled them to prevent model bias.
* **Data Wrangling:** Encoded categorical variables, and scaled features for model readiness.

### 2. Exploratory Data Analysis (EDA)
* **Correlation Analysis:** Analyzed relationships between borrower financial indicators and default risk to find the strongest predictors.
* **Regression Analysis:** Explored linear and logistic relationships among key lending variables.
* **Visualizations:** Generated distribution plots, heatmaps, and trend lines to understand borrower behavior.

### 3. Model Training & Predictive Analytics
* **Dataset Prediction:** Split the data into training and testing sets to evaluate model generalization.
* **Model Training:** Trained machine learning models (such as Logistic Regression ]) to predict loan default risks.
* **Testing & Evaluation:** Tested model performance using metrics like Accuracy, Precision, Recall, and F1-Score.

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
