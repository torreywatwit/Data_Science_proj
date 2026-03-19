import numpy as np
import pandas as pd
import matplotlib as plt

#First step is to clean our data

df = pd.read_csv("data/historicalcpi.csv")

print(df.head())
print(df.shape)
print(df.columns)

print(df.isna().sum())
print(df.duplicated().sum())

#after closer inspection, the missing values are percent changes in proccessed fruits and vegetables,
#assumingly from missing data, as filling those in would skew predictions, we will make a new dataset with those values omitted

clean_df = df.dropna()
print(clean_df.isna().sum())
print(clean_df.shape)
