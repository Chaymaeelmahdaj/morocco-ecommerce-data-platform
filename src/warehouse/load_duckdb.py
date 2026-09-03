from pathlib import Path
import duckdb


PROCESSED_DIR = Path("data/processed")
WAREHOUSE_DIR = Path("data/warehouse")

DATABASE_PATH = WAREHOUSE_DIR / "ecommerce.duckdb"


TABLES = {
    "customers": "customers.parquet",
    "orders": "orders.parquet",
    "order_items": "order_items.parquet",
    "payments": "payments.parquet",
    "reviews": "reviews.parquet",
    "products": "products.parquet",
    "sellers": "sellers.parquet",
    "geolocation": "geolocation.parquet",
    "category_translation": "category_translation.parquet",
}


def create_tables(connection):

    for table_name, filename in TABLES.items():

        parquet_path = PROCESSED_DIR / filename

        if not parquet_path.exists():
            raise FileNotFoundError(
                f"File not found: {parquet_path}"
            )

        print(f"Loading {table_name}...")

        connection.execute(
            f"""
            CREATE OR REPLACE TABLE {table_name} AS
            SELECT *
            FROM read_parquet('{parquet_path.as_posix()}')
            """
        )

        count = connection.execute(
            f"SELECT COUNT(*) FROM {table_name}"
        ).fetchone()[0]

        print(
            f"  ✓ {table_name}: {count:,} rows"
        )


def main():

    WAREHOUSE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print("=" * 70)
    print("DUCKDB DATA WAREHOUSE")
    print("=" * 70)

    connection = duckdb.connect(
        str(DATABASE_PATH)
    )

    try:

        create_tables(connection)

        print()
        print("Warehouse tables:")
        
        tables = connection.execute(
            "SHOW TABLES"
        ).fetchall()

        for table in tables:
            print(f"  ✓ {table[0]}")

        print()
        print(
            f"Database created at: {DATABASE_PATH}"
        )

    finally:
        connection.close()


if __name__ == "__main__":
    main()