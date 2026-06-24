import pandas as pd

# Load datasets
df1 = pd.read_csv("data/LOTR.csv")
df2 = pd.read_csv("data/LOTR2.csv")

# Inner merge (default) — only matching rows
df1.merge(df2, how='inner')

# Inner merge on specific columns
df1.merge(df2, how='inner', on=['FellowshipID', 'FirstName'])
df1.merge(df2, how='inner', on='FellowshipID')

# Outer merge — all rows from both DataFrames
df1.merge(df2, how='outer')

# Left merge — all rows from df1
df1.merge(df2, how='left')

# Right merge — all rows from df2
df1.merge(df2, how='right')

# Cross merge — every combination of rows
df1.merge(df2, how='cross')

# Join with suffix labels to avoid column name conflicts
df1.join(df2, on='FellowshipID', how='outer', lsuffix='_Left', rsuffix='_Right')

# Join using FellowshipID as index on both DataFrames
df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix='_Left', rsuffix='_Right')

# Concat side by side (axis=1) keeping only shared columns
pd.concat([df1, df2], join='inner', axis=1)

# Left merge on FellowshipID
df1.merge(df2, how='left', on='FellowshipID')
