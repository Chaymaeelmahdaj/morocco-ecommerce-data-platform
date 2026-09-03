import pandas as pd


def test_orders_order_id_unique():

    df = pd.read_parquet(
        "data/processed/orders.parquet"
    )

    assert df["order_id"].notna().all()
    assert df["order_id"].is_unique


def test_customers_customer_id_unique():

    df = pd.read_parquet(
        "data/processed/customers.parquet"
    )

    assert df["customer_id"].notna().all()
    assert df["customer_id"].is_unique


def test_products_product_id_unique():

    df = pd.read_parquet(
        "data/processed/products.parquet"
    )

    assert df["product_id"].notna().all()
    assert df["product_id"].is_unique


def test_sellers_seller_id_unique():

    df = pd.read_parquet(
        "data/processed/sellers.parquet"
    )

    assert df["seller_id"].notna().all()
    assert df["seller_id"].is_unique