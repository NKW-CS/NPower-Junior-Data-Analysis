import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# ------------------------------------------------------------
# Load dataset
# ------------------------------------------------------------

df = pd.read_csv("Loan_Default.csv")

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

# ------------------------------------------------------------
# Numeric cleanup
# ------------------------------------------------------------

numeric_columns = [
    "status",
    "credit_score",
    "rate_of_interest",
    "loan_amount",
    "income",
    "property_value",
    "interest_rate_spread",
    "dtir1",
    "month"
]

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ------------------------------------------------------------
# Date, year, and month handling
# ------------------------------------------------------------

if "date_of_the_loan" in df.columns:
    df["date_of_the_loan"] = pd.to_datetime(df["date_of_the_loan"], errors="coerce")
    df["year"] = df["date_of_the_loan"].dt.year

    if "month" not in df.columns:
        df["month"] = df["date_of_the_loan"].dt.month

elif "year" in df.columns:
    df["year"] = pd.to_numeric(df["year"], errors="coerce")

else:
    df["year"] = 2019

# If month is still missing, default to month 1
if "month" not in df.columns:
    df["month"] = 1

df["month"] = pd.to_numeric(df["month"], errors="coerce")

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

df["month_name"] = df["month"].map(month_names)

# ------------------------------------------------------------
# Readable labels
# ------------------------------------------------------------

df["loan_status"] = df["status"].map({
    0: "Non-Default",
    1: "Default"
})

df["loan_type_label"] = df["loan_type"].map({
    "type1": "Conventional",
    "type2": "FHA",
    "type3": "VA"
})

df["loan_type_label"] = df["loan_type_label"].fillna(df["loan_type"])

# ------------------------------------------------------------
# Clean rows needed for dashboard
# ------------------------------------------------------------

required_columns = [
    "region",
    "month",
    "month_name",
    "loan_type_label",
    "status",
    "credit_score",
    "rate_of_interest",
    "loan_status"
]

df = df.dropna(subset=required_columns)

# ------------------------------------------------------------
# Dash app
# ------------------------------------------------------------

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Loan Default Risk Analysis Dashboard",
        style={
            "textAlign": "center",
            "color": "#1f2937",
            "marginBottom": "5px"
        }
    ),

    html.P(
        "Interactive dashboard for exploring lending risk by region, month, loan type, loan status, credit score, and interest rate.",
        style={
            "textAlign": "center",
            "fontSize": "16px",
            "color": "#4b5563",
            "marginBottom": "20px"
        }
    ),

    html.Hr(),

    # Filters
    html.Div([

        html.Div([
            html.Label("Select Region", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="region_filter",
                options=[
                    {"label": region, "value": region}
                    for region in sorted(df["region"].dropna().unique())
                ],
                value=sorted(df["region"].dropna().unique()),
                multi=True
            )
        ], style={"width": "24%", "padding": "8px"}),

        html.Div([
            html.Label("Select Month", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="month_filter",
                options=[
                    {"label": month_names[int(month)], "value": int(month)}
                    for month in sorted(df["month"].dropna().unique())
                    if int(month) in month_names
                ],
                value=[
                    int(month)
                    for month in sorted(df["month"].dropna().unique())
                    if int(month) in month_names
                ],
                multi=True
            )
        ], style={"width": "24%", "padding": "8px"}),

        html.Div([
            html.Label("Select Loan Type", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="loan_type_filter",
                options=[
                    {"label": loan_type, "value": loan_type}
                    for loan_type in sorted(df["loan_type_label"].dropna().unique())
                ],
                value=sorted(df["loan_type_label"].dropna().unique()),
                multi=True
            )
        ], style={"width": "24%", "padding": "8px"}),

        html.Div([
            html.Label("Select Loan Status", style={"fontWeight": "bold"}),
            dcc.Dropdown(
                id="loan_status_filter",
                options=[
                    {"label": status, "value": status}
                    for status in sorted(df["loan_status"].dropna().unique())
                ],
                value=sorted(df["loan_status"].dropna().unique()),
                multi=True
            )
        ], style={"width": "24%", "padding": "8px"}),

    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "alignItems": "center",
        "marginBottom": "20px"
    }),

    # KPI Cards
    html.Div([

        html.Div([
            html.H3(id="total_applications", style={"fontSize": "26px"}),
            html.P("Total Applications")
        ], style={
            "flex": "1",
            "backgroundColor": "#f3f4f6",
            "padding": "20px",
            "margin": "8px",
            "textAlign": "center",
            "borderRadius": "12px",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"
        }),

        html.Div([
            html.H3(id="avg_credit_score", style={"fontSize": "26px"}),
            html.P("Average Credit Score")
        ], style={
            "flex": "1",
            "backgroundColor": "#f3f4f6",
            "padding": "20px",
            "margin": "8px",
            "textAlign": "center",
            "borderRadius": "12px",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"
        }),

        html.Div([
            html.H3(id="avg_interest_rate", style={"fontSize": "26px"}),
            html.P("Average Interest Rate")
        ], style={
            "flex": "1",
            "backgroundColor": "#f3f4f6",
            "padding": "20px",
            "margin": "8px",
            "textAlign": "center",
            "borderRadius": "12px",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"
        }),

        html.Div([
            html.H3(id="default_rate", style={"fontSize": "26px"}),
            html.P("Default Rate")
        ], style={
            "flex": "1",
            "backgroundColor": "#f3f4f6",
            "padding": "20px",
            "margin": "8px",
            "textAlign": "center",
            "borderRadius": "12px",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.08)"
        }),

    ], style={
        "display": "flex",
        "justifyContent": "space-between",
        "marginBottom": "30px"
    }),

    # Charts
    html.Div([

        html.Div([dcc.Graph(id="bar_chart")], style={
            "backgroundColor": "white",
            "padding": "15px",
            "borderRadius": "12px",
            "boxShadow": "0 2px 10px rgba(0,0,0,0.08)"
        }),

        html.Div([dcc.Graph(id="loan_type_chart")], style={
            "backgroundColor": "white",
            "padding": "15px",
            "borderRadius": "12px",
            "boxShadow": "0 2px 10px rgba(0,0,0,0.08)"
        }),

        html.Div([dcc.Graph(id="pie_chart")], style={
            "backgroundColor": "white",
            "padding": "15px",
            "borderRadius": "12px",
            "boxShadow": "0 2px 10px rgba(0,0,0,0.08)"
        }),

        html.Div([dcc.Graph(id="box_plot")], style={
            "backgroundColor": "white",
            "padding": "15px",
            "borderRadius": "12px",
            "boxShadow": "0 2px 10px rgba(0,0,0,0.08)"
        }),

    ], style={
        "display": "grid",
        "gridTemplateColumns": "1fr 1fr",
        "gap": "20px",
        "marginBottom": "25px"
    }),

    html.Div([dcc.Graph(id="heatmap_chart")], style={
        "backgroundColor": "white",
        "padding": "15px",
        "borderRadius": "12px",
        "boxShadow": "0 2px 10px rgba(0,0,0,0.08)"
    })

], style={
    "fontFamily": "Arial",
    "padding": "25px",
    "backgroundColor": "#f9fafb"
})


@app.callback(
    [
        Output("total_applications", "children"),
        Output("avg_credit_score", "children"),
        Output("avg_interest_rate", "children"),
        Output("default_rate", "children"),
        Output("bar_chart", "figure"),
        Output("loan_type_chart", "figure"),
        Output("pie_chart", "figure"),
        Output("box_plot", "figure"),
        Output("heatmap_chart", "figure")
    ],
    [
        Input("region_filter", "value"),
        Input("month_filter", "value"),
        Input("loan_type_filter", "value"),
        Input("loan_status_filter", "value")
    ]
)
def update_dashboard(selected_regions, selected_months, selected_loan_types, selected_loan_status):

    filtered_df = df[
        (df["region"].isin(selected_regions)) &
        (df["month"].isin(selected_months)) &
        (df["loan_type_label"].isin(selected_loan_types)) &
        (df["loan_status"].isin(selected_loan_status))
    ]

    if filtered_df.empty:
        empty_fig = px.scatter(title="No data available for selected filters")
        return (
            "0",
            "0",
            "0%",
            "0%",
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig
        )

    total_applications = f"{len(filtered_df):,}"
    avg_credit_score = f"{filtered_df['credit_score'].mean():.2f}"
    avg_interest_rate = f"{filtered_df['rate_of_interest'].mean():.2f}%"
    default_rate_value = f"{filtered_df['status'].mean() * 100:.2f}%"

    # Chart 1: Default Rate by Region
    region_default = filtered_df.groupby(
        "region",
        as_index=False
    )["status"].mean()

    bar_chart = px.bar(
        region_default,
        x="region",
        y="status",
        title="Average Default Rate by Region",
        labels={
            "region": "Region",
            "status": "Default Rate"
        },
        color="region"
    )
    bar_chart.update_yaxes(tickformat=".0%")
    bar_chart.update_layout(height=400, showlegend=False)

    # Chart 2: Default Rate by Loan Type
    loan_type_default = filtered_df.groupby(
        "loan_type_label",
        as_index=False
    )["status"].mean()

    loan_type_chart = px.bar(
        loan_type_default,
        x="loan_type_label",
        y="status",
        title="Default Rate by Loan Type",
        labels={
            "loan_type_label": "Loan Type",
            "status": "Default Rate"
        },
        color="loan_type_label"
    )
    loan_type_chart.update_yaxes(tickformat=".0%")
    loan_type_chart.update_layout(height=400, showlegend=False)

    # Chart 3: Loan Type Distribution
    pie_chart = px.pie(
        filtered_df,
        names="loan_type_label",
        title="Loan Type Distribution"
    )
    pie_chart.update_layout(height=400)

    # Chart 4: Credit Score Distribution by Loan Status
    box_plot = px.box(
        filtered_df,
        x="loan_status",
        y="credit_score",
        title="Credit Score Distribution by Loan Status",
        labels={
            "loan_status": "Loan Status",
            "credit_score": "Credit Score"
        },
        color="loan_status"
    )
    box_plot.update_layout(height=400, showlegend=False)

    # Chart 5: Heatmap
    heatmap_data = filtered_df.pivot_table(
        index="region",
        columns="loan_type_label",
        values="status",
        aggfunc="mean"
    )

    heatmap_chart = px.imshow(
        heatmap_data,
        text_auto=".1%",
        title="Default Rate Heatmap by Region and Loan Type",
        labels=dict(color="Default Rate"),
        aspect="auto"
    )
    heatmap_chart.update_layout(height=450)

    return (
        total_applications,
        avg_credit_score,
        avg_interest_rate,
        default_rate_value,
        bar_chart,
        loan_type_chart,
        pie_chart,
        box_plot,
        heatmap_chart
    )


if __name__ == "__main__":
    app.run(debug=True)