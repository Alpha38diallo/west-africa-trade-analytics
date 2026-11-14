import pandas as pd

imports = pd.read_csv(
    "data/processed/imports_west_africa.csv"
)

exports = pd.read_csv(
    "data/processed/exports_west_africa.csv"
)

imports = imports[
    ["REF_AREA_LABEL", "TIME_PERIOD", "OBS_VALUE"]
].copy()

exports = exports[
    ["REF_AREA_LABEL", "TIME_PERIOD", "OBS_VALUE"]
].copy()

imports.columns = [
    "country",
    "year",
    "imports"
]

exports.columns = [
    "country",
    "year",
    "exports"
]

trade = pd.merge(
    exports,
    imports,
    on=["country", "year"],
    how="inner"
)

trade["balance"] = (
    trade["exports"]
    - trade["imports"]
)

trade.to_csv(
    "data/processed/trade_balance.csv",
    index=False
)

print(trade.head())
print("\nTrade balance file created successfully")