import pandas as pd

orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

print(orders.head())

print("\nShape:")
print(orders.shape)

print("\nOrder status:")
print(orders["order_status"].value_counts())

print("\nDate range:")
print(
    orders["order_purchase_timestamp"].min(),
    "→",
    orders["order_purchase_timestamp"].max()
)
orders = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)
print(
    "Duplicate orders:",
    orders["order_id"].duplicated().sum()
)
missing = (
    orders.isna()
    .sum()
    .sort_values(ascending=False)
)

print(missing)