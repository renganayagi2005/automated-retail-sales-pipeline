import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_sales.csv")

# Top 5 selling products
top_products = df.groupby("product_name")["total_sales"].sum().sort_values(ascending=False)

print("Top 5 Products:")
print(top_products.head())

# Total revenue
total_revenue = df["total_sales"].sum()

print("\nTotal Revenue:")
print(total_revenue)

# Sales by category
category_sales = df.groupby("category")["total_sales"].sum()

print("\nSales by Category:")
print(category_sales)

import matplotlib.pyplot as plt

# Sales by category chart
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

# Save chart
plt.savefig("../charts/category_sales.png")

print("\nChart saved successfully!")