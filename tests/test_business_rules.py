import pandas as pd


def test_order_items_price():

    df = pd.read_parquet(
        "data/processed/order_items.parquet"
    )

    assert (df["price"] > 0).all()


def test_freight_value():

    df = pd.read_parquet(
        "data/processed/order_items.parquet"
    )

    assert (df["freight_value"] >= 0).all()


def test_payment_value():

    df = pd.read_parquet(
        "data/processed/payments.parquet"
    )

    assert (df["payment_value"] >= 0).all()


def test_review_score():

    df = pd.read_parquet(
        "data/processed/reviews.parquet"
    )

    assert df["review_score"].between(1, 5).all()