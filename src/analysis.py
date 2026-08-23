import pandas as pd

# Load the sales data
sales = pd.read_csv("data/sales.csv")

# Show the first 5 rows
print("First 5 rows:")
print(sales.head())

# Show information about the data
print("\nDataset information:")
print(sales.info())

# Calculate total revenue
total_revenue = sales["revenue"].sum()

print("\nTotal revenue:")
print(total_revenue)
