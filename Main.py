import pandas as pd

dfs = pd.read_excel(io="WineKMC.xlsx",sheet_name="Pivot", usecols= "A:CW", skiprows=3, nrows=32)

dfs = dfs.fillna(0)

print(dfs)
# print(dfs["Unnameded"])

# Write section of XLSX file to CSV.
# dfs.to_csv("section.csv")