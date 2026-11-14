import pandas as pd
from pathlib import Path

WEST_AFRICA = [
    "Guinea",
    "Senegal",
    "Mali",
    "Côte d’Ivoire",
    "Liberia",
    "Sierra Leone",
    "Ghana",
    "Nigeria",
    "Burkina Faso",
    "Guinea-Bissau"
]

imports = pd.read_csv("data/raw/imports.csv")
exports = pd.read_csv("data/raw/exports.csv")

imports_filtered = imports[
    imports["REF_AREA_LABEL"].isin(WEST_AFRICA)
]

exports_filtered = exports[
    exports["REF_AREA_LABEL"].isin(WEST_AFRICA)
]

Path("data/processed").mkdir(parents=True, exist_ok=True)

imports_filtered.to_csv(
    "data/processed/imports_west_africa.csv",
    index=False
)

exports_filtered.to_csv(
    "data/processed/exports_west_africa.csv",
    index=False
)

print("Files saved successfully")