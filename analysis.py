import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# Create Customers Dataset
# -----------------------------

regions = ["Northeast", "South", "Midwest", "West"]
segments = ["Corporate", "Small Business", "Consumer"]
industries = [
    "Technology",
    "Healthcare",
    "Finance",
    "Retail",
    "Media",
    "Education"
]

customers = []

for i in range(1, 501):
    customers.append({
        "Customer_ID": f"C{i:04d}",
        "Customer_Name": fake.company(),
        "Region": random.choice(regions),
        "Customer_Segment": random.choice(segments),
        "Industry": random.choice(industries)
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/customers.csv",
    index=False
)


# -----------------------------
# Create Products Dataset
# -----------------------------

products_list = [
    ("Cloud Analytics Platform", "Software"),
    ("Business Laptop", "Hardware"),
    ("Cybersecurity Package", "Software"),
    ("Network Equipment", "Hardware"),
    ("Analytics Consulting", "Services"),
    ("Data Storage Solution", "Software"),
    ("Office Equipment", "Hardware"),
    ("Training Services", "Services")
]

products = []

for i in range(1, 51):
    product = random.choice(products_list)

    products.append({
        "Product_ID": f"P{i:03d}",
        "Product_Name": product[0],
        "Category": product[1],
        "Unit_Cost": random.randint(100,1000)
    })


products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/products.csv",
    index=False
)


# -----------------------------
# Create Orders Dataset
# -----------------------------

orders = []

start_date = datetime(2025,1,1)

for i in range(1,5001):

    order_date = start_date + timedelta(
        days=random.randint(0,365)
    )

    orders.append({
        "Order_ID": f"O{i:05d}",
        "Customer_ID": f"C{random.randint(1,500):04d}",
        "Product_ID": f"P{random.randint(1,50):03d}",
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Quantity": random.randint(1,10)
    })


orders_df = pd.DataFrame(orders)


orders_df.to_csv(
    "data/orders.csv",
    index=False
)


# -----------------------------
# Create Transactions Dataset
# -----------------------------

transactions = []

for i in range(1,5001):

    revenue = random.randint(500,10000)

    profit = round(
        revenue * random.uniform(0.15,0.45),
        2
    )

    discount = round(
        random.uniform(0,0.20),
        2
    )

    transactions.append({
        "Transaction_ID": f"T{i:05d}",
        "Order_ID": f"O{i:05d}",
        "Revenue": revenue,
        "Profit": profit,
        "Discount": discount
    })


transactions_df = pd.DataFrame(transactions)


transactions_df.to_csv(
    "data/transactions.csv",
    index=False
)


print("Business Operations dataset created successfully!")

print("\nCustomers Preview:")
print(customers_df.head())

print("\nOrders Preview:")
print(orders_df.head())

print("\nTransactions Preview:")
print(transactions_df.head())

print("\nDataset Sizes:")
print("Customers:", customers_df.shape)
print("Products:", products_df.shape)
print("Orders:", orders_df.shape)
print("Transactions:", transactions_df.shape)