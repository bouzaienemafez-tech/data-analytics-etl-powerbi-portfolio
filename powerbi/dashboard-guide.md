# Power BI Dashboard Guide

## Load data

Run the ETL pipeline, then use **Get Data → SQLite database** to load `sales_analytics.db`. Import `fact_sales` and all dimension tables. Create relationships from each dimension key to the matching key in `fact_sales`.

## Measures

```DAX
Total Revenue = SUM(fact_sales[revenue])
Total Profit = SUM(fact_sales[profit])
Total Orders = DISTINCTCOUNT(fact_sales[order_id])
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

## One-page layout

- KPI cards: Total Revenue, Total Profit, Profit Margin %, Total Orders.
- Line chart: Total Revenue by `dim_date[full_date]`.
- Clustered column chart: Total Profit by `dim_product[category]`.
- Bar chart: Total Revenue by `fact_sales[region]`.
- Donut chart: Total Revenue by `dim_customer[segment]`.
- Slicers: year, region and category.

Use a neutral background, one accent colour for revenue and a contrasting colour for profit. Add clear titles and currency formatting.
