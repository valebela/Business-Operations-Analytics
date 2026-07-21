import pandas as pd


# Load datasets

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
transactions = pd.read_csv("data/transactions.csv")


# Combine datasets

sales = orders.merge(
    transactions,
    on="Order_ID"
)

sales = sales.merge(
    customers,
    on="Customer_ID"
)

sales = sales.merge(
    products,
    on="Product_ID"
)


print("Combined Dataset:")
print(sales.head())


# -----------------------------
# Revenue by Region
# -----------------------------

region_revenue = (
    sales.groupby("Region")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


print("\nRevenue by Region:")
print(region_revenue)


# -----------------------------
# Profit by Industry
# -----------------------------

industry_profit = (
    sales.groupby("Industry")["Profit"]
    .sum()
    .sort_values(ascending=False)
)


print("\nProfit by Industry:")
print(industry_profit)


# -----------------------------
# Product Performance
# -----------------------------

product_sales = (
    sales.groupby("Product_Name")
    ["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


print("\nTop Products:")
print(product_sales)


# -----------------------------
# Export Tableau Dataset
# -----------------------------

sales.to_csv(
    "tableau/business_sales_dashboard.csv",
    index=False
)


print("\nAnalysis complete!")

# -----------------------------
# KPI Metrics
# -----------------------------

total_revenue = sales["Revenue"].sum()

total_profit = sales["Profit"].sum()

total_orders = sales["Order_ID"].nunique()

average_order_value = total_revenue / total_orders

profit_margin = (total_profit / total_revenue) * 100


print("\nBusiness KPIs:")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")# -----------------------------
# KPI Metrics
# -----------------------------

total_revenue = sales["Revenue"].sum()

total_profit = sales["Profit"].sum()

total_orders = sales["Order_ID"].nunique()

average_order_value = total_revenue / total_orders

profit_margin = (total_profit / total_revenue) * 100

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")