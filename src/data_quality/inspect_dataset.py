from pathlib import Path
import pandas as pd


RAW_DATA = Path("data/raw")


def inspect_file(file_path: Path):
    print("=" * 70)
    print(f"FILE: {file_path.name}")
    print("=" * 70)

    df = pd.read_csv(file_path)

    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)

    print()


def main():
    csv_files = sorted(RAW_DATA.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/raw/")
        return

    for file_path in csv_files:
        inspect_file(file_path)


if __name__ == "__main__":
    main()