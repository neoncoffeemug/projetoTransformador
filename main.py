import pandas as pd

df1 = pd.read_csv("JAN_JUN_2025.csv", encoding='utf-8', sep=';')
df2 = pd.read_csv("JUL_DEZ_2025.csv", encoding='utf-8', sep=';')
full_df = pd.concat([df1, df2], ignore_index=True)

row_count = len(full_df.index)
print(row_count)

print(full_df.info())

full_df_clean = full_df.dropna()
print(full_df_clean.info())