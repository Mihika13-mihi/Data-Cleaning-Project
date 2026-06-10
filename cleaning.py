import pandas as pd

df = pd.read_csv("data.csv")

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")

df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaning completed!")