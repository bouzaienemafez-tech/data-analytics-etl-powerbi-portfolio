# Sales Analytics: SQL, ETL & Power BI

An end-to-end portfolio project that turns raw retail CSV files into an analytics-ready star schema. It demonstrates practical data-cleaning, SQL reporting, and Power BI dashboard design.

## What this project covers

- **ETL:** Python pipeline validates, standardises and loads raw order data into SQLite.
- **Data modelling:** A fact table (`fact_sales`) joined to `dim_customer`, `dim_product` and `dim_date` dimensions.
- **SQL analytics:** Revenue, profit, growth, product performance and customer segmentation queries.
- **Power BI:** A clear dashboard blueprint with DAX measures and recommended visuals.

## Structure

```
data/raw/                 Source CSV files
src/etl.py                Extract, transform and load pipeline
sql/01_schema.sql         Star-schema DDL
sql/02_analysis.sql       Business analysis queries
powerbi/dashboard-guide.md Dashboard layout and DAX measures
```

## Run locally

```bash
python3 src/etl.py
sqlite3 data/warehouse/sales_analytics.db < sql/02_analysis.sql
```

The pipeline creates `data/warehouse/sales_analytics.db`. It uses only the Python standard library.

## Dashboard questions answered

1. How are revenue, profit and orders trending over time?
2. Which categories and products drive the most profit?
3. Which customer segments are most valuable?
4. Which regions are underperforming?

## Skills demonstrated

`Python` · `ETL` · `Data Quality` · `SQL` · `Star Schema` · `SQLite` · `Power BI` · `DAX`
