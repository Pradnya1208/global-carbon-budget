import pandas as pd

from util import root, excel_global

land_use_csv = root / "data/land-use-change.csv"

# Land-use change emissions
landuse_change = pd.read_excel(
    excel_global,
    sheet_name="Land-Use Change Emissions",
    skiprows=25,
    index_col="Year",
    usecols="A:B,D,E,G:U,X",
)

landuse_change.rename(
    columns={n: n.strip() for n in landuse_change.columns}, inplace=True
)
landuse_change.rename(columns={"GCB": "Land-Use-Change"}, inplace=True)

landuse_change.to_csv(land_use_csv, float_format="%.3f", encoding="UTF-8")
