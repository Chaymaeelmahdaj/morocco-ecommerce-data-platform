from pathlib import Path
import duckdb


DATABASE_PATH = Path(
    "data/warehouse/ecommerce.duckdb"
)


def main():

    connection = duckdb.connect(
        str(DATABASE_PATH)
    )

    print("=" * 70)
    print("DUCKDB ANALYTICS")
    print("=" * 70)

    print("\n1. Total customers")

    result = connection.execute(
        """
        SELECT COUNT(*) AS total_customers
        FROM customers
        """
    ).fetchone()

    print(result[0])

    print("\n2. Total orders")

    result = connection.execute(
        """
        SELECT COUNT(*) AS total_orders
        FROM orders
        """
    ).fetchone()

    print(result[0])

    print("\n3. Orders by status")

    result = connection.execute(
        """
        SELECT
            order_status,
            COUNT(*) AS order_count
        FROM orders
        GROUP BY order_status
        ORDER BY order_count DESC
        """
    ).fetchall()

    for row in result:
        print(row)

    print("\n4. Total product revenue")

    result = connection.execute(
        """
        SELECT
            ROUND(SUM(price), 2)
        FROM order_items
        """
    ).fetchone()

    print(result[0])

    connection.close()


if __name__ == "__main__":
    main()