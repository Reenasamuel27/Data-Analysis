import pandas as pd 
# Load dataset
df = pd.read_csv("sales_data.csv") 

# Display first few rows
print(df.head()) 

# Get basic information
print(df.info()) 

# Check missing values
print(df.isnull().sum())

# Fill missing values
df.fillna(0, inplace=True) 

# Convert date column to datetime format
df['Date'] = pd.to_datetime(df['Date']) 

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Total Revenue
total_revenue = df["Revenue"].sum()
print(f"Total Revenue: {total_revenue}") 

# Top Selling Products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(top_products) 

# Monthly Sales Trend
df["Month"] = df["Date"].dt.to_period("M") 
monthly_sales = df.groupby("Month")["Revenue"].sum()
print(monthly_sales)

import matplotlib.pyplot as plt
import seaborn as sns
 
# Sales Trend Over Time
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales, marker="o")
plt.title("Monthly Sales Revenue")
plt.xticks(rotation=45)
plt.show()
 
# Top Selling Products Bar Chart
top_products.plot(kind="bar", figsize=(8, 4))
plt.title("Top Selling Products")
plt.ylabel("Revenue")
plt.show()
