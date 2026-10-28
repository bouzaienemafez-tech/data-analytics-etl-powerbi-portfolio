PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS dim_customer (
  customer_key INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL UNIQUE,
  segment TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_product (
  product_key INTEGER PRIMARY KEY,
  product_name TEXT NOT NULL UNIQUE,
  category TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS dim_date (
  date_key INTEGER PRIMARY KEY,
  full_date TEXT NOT NULL UNIQUE,
  year INTEGER NOT NULL,
  month INTEGER NOT NULL,
  month_name TEXT NOT NULL,
  quarter TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_sales (
  order_id INTEGER PRIMARY KEY,
  date_key INTEGER NOT NULL REFERENCES dim_date(date_key),
  customer_key INTEGER NOT NULL REFERENCES dim_customer(customer_key),
  product_key INTEGER NOT NULL REFERENCES dim_product(product_key),
  region TEXT NOT NULL,
  quantity INTEGER NOT NULL CHECK(quantity > 0),
  unit_price REAL NOT NULL CHECK(unit_price >= 0),
  discount_pct REAL NOT NULL CHECK(discount_pct BETWEEN 0 AND 1),
  revenue REAL NOT NULL,
  cost REAL NOT NULL,
  profit REAL NOT NULL
);
