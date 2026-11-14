import pandas as pd
import plotly.express as px
from pathlib import Path

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

Path("visualizations").mkdir(exist_ok=True)

regional_events = {
    2008: "Financial Crisis",
    2014: "Ebola",
    2020: "COVID-19"
}

guinea_events = {
    2008: "Financial Crisis",
    2014: "Ebola",
    2016: "Ebola Ends",
    2020: "COVID-19",
    2021: "Guinea Coup"
}

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("data/processed/trade_balance.csv")

df["year"] = pd.to_numeric(df["year"])

df = df.sort_values(["country", "year"])

# --------------------------------------------------
# 1. WEST AFRICA IMPORTS VS EXPORTS
# --------------------------------------------------

overview = (
    df.groupby("year")[["exports", "imports"]]
      .sum()
      .reset_index()
)

fig = px.line(
    overview,
    x="year",
    y=["exports", "imports"],
    title="West Africa Imports vs Exports (1960-2025)"
)

regional_positions = {
    2008: 0.85,
    2014: 0.60,
    2020: 0.35
}

for year, label in regional_events.items():

    fig.add_vline(
        x=year,
        line_dash="dot",
        line_color="red",
        line_width=3,
        opacity=0.8
    )

    fig.add_annotation(
        x=year,
        y=regional_positions[year],
        yref="paper",
        text=label,
        showarrow=False,
        textangle=-90,
        font=dict(
            size=20,
            color="darkgreen"
        )
    )

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="US Dollars",
    hovermode="x unified"
)

fig.write_html(
    "visualizations/west_africa_trade_overview.html"
)

print("west_africa_trade_overview.html created")

# --------------------------------------------------
# 2. WEST AFRICA TRADE BALANCE
# --------------------------------------------------

balance = (
    df.groupby("year")["balance"]
      .sum()
      .reset_index()
)

fig = px.line(
    balance,
    x="year",
    y="balance",
    title="West Africa Trade Balance (1960-2025)"
)

regional_positions = {
    2008: 0.85,
    2014: 0.60,
    2020: 0.35
}

for year, label in regional_events.items():

    fig.add_vline(
        x=year,
        line_dash="dot",
        line_color="red",
        line_width=3,
        opacity=0.8
    )

    fig.add_annotation(
        x=year,
        y=regional_positions[year],
        yref="paper",
        text=label,
        showarrow=False,
        textangle=-90,
        font=dict(
            size=20,
            color="darkgreen"
        )
    )

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Trade Balance (US$)",
    hovermode="x unified"
)

fig.write_html(
    "visualizations/trade_balance.html"
)

print("trade_balance.html created")

# --------------------------------------------------
# 3. GUINEA IMPORTS VS EXPORTS
# --------------------------------------------------

guinea = (
    df[df["country"] == "Guinea"]
    .sort_values("year")
)

fig = px.line(
    guinea,
    x="year",
    y=["exports", "imports"],
    title="Guinea Imports vs Exports (1986-2025)"
)

guinea_positions = {
    2008: 0.85,
    2014: 0.70,
    2016: 0.55,
    2020: 0.40,
    2021: 0.25
}

for year, label in guinea_events.items():

    # Ligne verticale rouge
    fig.add_vline(
        x=year,
        line_dash="dot",
        line_color="red",
        line_width=3,
        opacity=0.8
    )

    # Label vert
    fig.add_annotation(
        x=year,
        y=guinea_positions[year],
        yref="paper",
        text=label,
        showarrow=False,
        textangle=-90,
        font=dict(
            size=20,
            color="darkgreen"
        )
    )

fig.add_annotation(
    x=2025,
    y=guinea["exports"].max(),
    text="Simandou Outlook",
    showarrow=True,
    arrowhead=2,
    arrowwidth=2,
    arrowcolor="darkgreen",
    font=dict(
        size=20,
        color="darkgreen"
    )
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="US Dollars",
    hovermode="x unified"
)

fig.write_html(
    "visualizations/guinea_trade_analysis.html"
)

print("guinea_trade_analysis.html created")

# --------------------------------------------------
# 4. GUINEA TRADE BALANCE
# --------------------------------------------------

fig = px.line(
    guinea,
    x="year",
    y="balance",
    title="Guinea Trade Balance (1986-2025)"
)

guinea_positions = {
    2008: 0.85,
    2014: 0.70,
    2016: 0.55,
    2020: 0.40,
    2021: 0.25
}

for year, label in guinea_events.items():

    # Ligne verticale rouge
    fig.add_vline(
        x=year,
        line_dash="dot",
        line_color="red",
        line_width=3,
        opacity=0.8
    )

    # Label vert
    fig.add_annotation(
        x=year,
        y=guinea_positions[year],
        yref="paper",
        text=label,
        showarrow=False,
        textangle=-90,
        font=dict(
            size=20,
            color="darkgreen"
        )
    )

fig.add_annotation(
    x=2025,
    y=guinea["balance"].max(),
    text="Simandou Outlook",
    showarrow=True,
    arrowhead=2,
    arrowwidth=2,
    arrowcolor="darkgreen",
    font=dict(
        size=20,
        color="darkgreen"
    )
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Trade Balance (US$)",
    hovermode="x unified"
)

fig.write_html(
    "visualizations/guinea_trade_balance.html"
)

print("guinea_trade_balance.html created")

# --------------------------------------------------
# 5. WEST AFRICA EXPORT COMPARISON
# --------------------------------------------------

comparison_countries = [
    "Ghana",
    "Côte d’Ivoire",
    "Guinea",
    "Senegal",
    "Burkina Faso"
]

comparison = (
    df[df["country"].isin(comparison_countries)]
    .sort_values(["country", "year"])
)

fig = px.line(
    comparison,
    x="year",
    y="exports",
    color="country",
    title="West Africa Export Comparison (1960-2025)"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Exports (US$)",
    hovermode="x unified"
)

fig.write_html(
    "visualizations/west_africa_comparison.html"
)