"""Load raw retail orders into an analytics-ready SQLite star schema."""
import csv
import sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data/raw/orders.csv"
DB_FILE = ROOT / "data/warehouse/sales_analytics.db"
SCHEMA_FILE = ROOT / "sql/01_schema.sql"


def clean_text(value):
    return " ".join(value.strip().split())


def load():
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_FILE)
    connection.executescript(SCHEMA_FILE.read_text())

    with RAW_FILE.open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            order_id = int(row["order_id"])
            order_date = datetime.strptime(row["order_date"], "%Y-%m-%d")
            customer = clean_text(row["customer_name"])
            segment = clean_text(row["segment"])
            product = clean_text(row["product_name"])
            category = clean_text(row["category"])
            region = clean_text(row["region"])
            price, quantity = float(row["unit_price"]), int(row["quantity"])
            discount, unit_cost = float(row["discount_pct"]), float(row["cost_per_unit"])

            if not customer or not product or quantity <= 0 or not 0 <= discount <= 1:
                raise ValueError(f"Invalid data in order {order_id}")

            connection.execute("INSERT OR IGNORE INTO dim_customer(customer_name, segment) VALUES (?, ?)", (customer, segment))
            connection.execute("INSERT OR IGNORE INTO dim_product(product_name, category) VALUES (?, ?)", (product, category))
            date_key = int(order_date.strftime("%Y%m%d"))
            connection.execute(
                "INSERT OR IGNORE INTO dim_date VALUES (?, ?, ?, ?, ?, ?)",
                (date_key, order_date.date().isoformat(), order_date.year, order_date.month, order_date.strftime("%B"), f"Q{(order_date.month - 1)//3 + 1}"),
            )
            customer_key = connection.execute("SELECT customer_key FROM dim_customer WHERE customer_name = ?", (customer,)).fetchone()[0]
            product_key = connection.execute("SELECT product_key FROM dim_product WHERE product_name = ?", (product,)).fetchone()[0]
            revenue = round(price * quantity * (1 - discount), 2)
            cost = round(unit_cost * quantity, 2)
            connection.execute(
                "INSERT OR REPLACE INTO fact_sales VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (order_id, date_key, customer_key, product_key, region, quantity, price, discount, revenue, cost, round(revenue - cost, 2)),
            )

    connection.commit()
    count = connection.execute("SELECT COUNT(*) FROM fact_sales").fetchone()[0]
    connection.close()
    print(f"Loaded {count} orders into {DB_FILE}")


if __name__ == "__main__":
    load()
