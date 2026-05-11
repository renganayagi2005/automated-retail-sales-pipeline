import pandas as pd

# Load dataset
df = pd.read_csv("../data/sales.csv.csv")

# First 5 rows
print("First 5 Rows:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Create total_sales column
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["total_sales"] = df["sales"] * df["quantity"]

# Show updated dataset
print("\nDataset with Total Sales:")
print(df[["product_name", "sales", "quantity", "total_sales"]].head())

# Save cleaned dataset
df.to_csv("../data/cleaned_sales.csv", index=False)
print("\nCleaned dataset saved successfully!")