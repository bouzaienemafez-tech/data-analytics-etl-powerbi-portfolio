-- Executive KPIs
SELECT ROUND(SUM(revenue), 2) AS total_revenue,
       ROUND(SUM(profit), 2) AS total_profit,
       COUNT(*) AS orders,
       ROUND(SUM(revenue) / COUNT(*), 2) AS average_order_value
FROM fact_sales;

-- Monthly performance
SELECT d.year, d.month_name, ROUND(SUM(f.revenue), 2) AS revenue,
       ROUND(SUM(f.profit), 2) AS profit
FROM fact_sales f JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.year, d.month, d.month_name
ORDER BY d.year, d.month;

-- Category profitability
SELECT p.category, ROUND(SUM(f.revenue), 2) AS revenue,
       ROUND(SUM(f.profit), 2) AS profit,
       ROUND(100.0 * SUM(f.profit) / SUM(f.revenue), 1) AS profit_margin_pct
FROM fact_sales f JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.category ORDER BY profit DESC;

-- Customer segments and regional performance
SELECT c.segment, f.region, ROUND(SUM(f.revenue), 2) AS revenue, ROUND(SUM(f.profit), 2) AS profit
FROM fact_sales f JOIN dim_customer c ON f.customer_key = c.customer_key
GROUP BY c.segment, f.region ORDER BY profit DESC;
