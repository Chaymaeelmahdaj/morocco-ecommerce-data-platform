from pathlib import Path
import pandas as pd


PROCESSED_DIR = Path("data/processed")


EXPECTED_ROWS = {
    "customers.parquet": 99441,
    "geolocation.parquet": 1000163,
    "order_items.parquet": 112650,
    "payments.parquet": 103886,
    "reviews.parquet": 99224,
    "orders.parquet": 99441,
    "products.parquet": 32951,
    "sellers.parquet": 3095,
    "category_translation.parquet": 71,
}


def main():

    print("=" * 70)
    print("VALIDATING PROCESSED DATA")
    print("=" * 70)

    errors = 0

    for filename, expected_rows in EXPECTED_ROWS.items():

        path = PROCESSED_DIR / filename

        if not path.exists():
            print(f"❌ Missing: {filename}")
            errors += 1
            continue

        df = pd.read_parquet(path)

        actual_rows = len(df)

        if actual_rows == expected_rows:
            print(
                f"✓ {filename}: "
                f"{actual_rows:,} rows"
            )
        else:
            print(
                f"❌ {filename}: "
                f"expected {expected_rows:,}, "
                f"got {actual_rows:,}"
            )
            errors += 1

    print()

    if errors == 0:
        print("✅ All validations passed.")
    else:
        print(f"❌ {errors} validation(s) failed.")


if __name__ == "__main__":
    main()