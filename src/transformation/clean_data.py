from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean string columns:
    - Remove leading/trailing spaces
    - Keep missing values as missing
    """
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = df[column].apply(
            lambda x: x.strip() if isinstance(x, str) else x
        )

    return df


def process_customers():
    file = RAW_DIR / "olist_customers_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    df["customer_zip_code_prefix"] = (
        df["customer_zip_code_prefix"].astype("int64")
    )

    output = PROCESSED_DIR / "customers.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ customers: {len(df):,} rows")


def process_orders():
    file = RAW_DIR / "olist_orders_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    output = PROCESSED_DIR / "orders.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ orders: {len(df):,} rows")


def process_order_items():
    file = RAW_DIR / "olist_order_items_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    df["shipping_limit_date"] = pd.to_datetime(
        df["shipping_limit_date"],
        errors="coerce"
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df["freight_value"] = pd.to_numeric(
        df["freight_value"],
        errors="coerce"
    )

    output = PROCESSED_DIR / "order_items.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ order_items: {len(df):,} rows")


def process_payments():
    file = RAW_DIR / "olist_order_payments_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    df["payment_value"] = pd.to_numeric(
        df["payment_value"],
        errors="coerce"
    )

    output = PROCESSED_DIR / "payments.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ payments: {len(df):,} rows")


def process_reviews():
    file = RAW_DIR / "olist_order_reviews_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    date_columns = [
        "review_creation_date",
        "review_answer_timestamp",
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    output = PROCESSED_DIR / "reviews.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ reviews: {len(df):,} rows")


def process_products():
    file = RAW_DIR / "olist_products_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    numeric_columns = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    output = PROCESSED_DIR / "products.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ products: {len(df):,} rows")


def process_sellers():
    file = RAW_DIR / "olist_sellers_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    df["seller_zip_code_prefix"] = (
        df["seller_zip_code_prefix"].astype("int64")
    )

    output = PROCESSED_DIR / "sellers.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ sellers: {len(df):,} rows")


def process_geolocation():
    file = RAW_DIR / "olist_geolocation_dataset.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    df["geolocation_lat"] = pd.to_numeric(
        df["geolocation_lat"],
        errors="coerce"
    )

    df["geolocation_lng"] = pd.to_numeric(
        df["geolocation_lng"],
        errors="coerce"
    )

    output = PROCESSED_DIR / "geolocation.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ geolocation: {len(df):,} rows")


def process_category_translation():
    file = RAW_DIR / "product_category_name_translation.csv"

    df = pd.read_csv(file)

    df = clean_text_columns(df)

    output = PROCESSED_DIR / "category_translation.parquet"
    df.to_parquet(output, index=False)

    print(f"✓ category_translation: {len(df):,} rows")


def main():

    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\nStarting data transformation...\n")

    process_customers()
    process_orders()
    process_order_items()
    process_payments()
    process_reviews()
    process_products()
    process_sellers()
    process_geolocation()
    process_category_translation()

    print("\nTransformation completed successfully.")


if __name__ == "__main__":
    main()