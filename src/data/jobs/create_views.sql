/*
company_metrics_view provides an overview of company metrics, including profile information and historical price data, grouped by year and ticker.
*/

CREATE OR REPLACE VIEW company_metrics_view AS
SELECT 
    chd.ticker, 
    cp.name, 
    cp.industry, 
    cp.industry_key, 
    cp.sector, 
    cp.sector_key, 
    cp.country, 
    cp.website, 
    cp.market_cap, 
    cp.employees,
    EXTRACT(YEAR FROM chd.date) AS year, 
	AVG(chd.price) AS avg_price, 
    MIN(chd.price) AS min_price, 
    MAX(chd.price) AS max_price
FROM 
    public.company_historical_data chd
JOIN 
    public.company_profiles cp
ON 
    chd.ticker = cp.ticker
GROUP BY 
    year, chd.ticker, cp.id, cp.name, cp.industry, cp.industry_key, cp.sector, cp.sector_key, cp.country, cp.website, cp.market_cap, cp.employees
ORDER BY 
    year, avg_price DESC;



/*
senator_trades_view details senator transactions and ticker price movement up or down within a 5 day window
*/

CREATE OR REPLACE VIEW senator_trades_view AS

SELECT 
    t.senator_name,
    t.owner,
    t.transaction_date,
    t.ticker,
    t.amount,
    h.date AS close_date,
    h.price,
    LAG(h.price, 1) OVER (PARTITION BY t.ticker ORDER BY h.date) AS prev_close,
    LEAD(h.price, 1) OVER (PARTITION BY t.ticker ORDER BY h.date) AS next_close,
    CASE 
        WHEN LEAD(h.price, 1) OVER (PARTITION BY t.ticker ORDER BY h.date) > h.price 
        THEN ((LEAD(h.price, 1) OVER (PARTITION BY t.ticker ORDER BY h.date) - h.price) / h.price) * 100
        ELSE NULL
    END AS percentage_increase,
    CASE 
        WHEN LEAD(h.price, 1) OVER (PARTITION BY t.ticker ORDER BY h.date) < h.price 
        THEN ((h.price - LEAD(h.price, 1) OVER (PARTITION BY t.ticker ORDER BY h.date)) / h.price) * 100
        ELSE NULL
    END * -1 AS percentage_decrease
FROM 
    senator_trades t
JOIN 
    company_historical_data h
ON 
    t.ticker = h.ticker
AND 
    h.date BETWEEN t.transaction_date - INTERVAL '5 day' AND t.transaction_date + INTERVAL '5 day'
ORDER BY 
    t.ticker, t.transaction_date, h.date;


/*
view top_industries_view provides view of industry and sector sorted in descending by the market cap aggregate
*/

CREATE OR REPLACE VIEW top_industries_view AS
SELECT 
    cp.industry, 
    cp.industry_key, 
    cp.sector, 
    cp.sector_key, 
    SUM(cp.market_cap)
   
FROM 
    public.company_historical_data chd
JOIN 
    public.company_profiles cp
ON 
    chd.ticker = cp.ticker
GROUP BY 
        cp.industry, 
    cp.industry_key, 
    cp.sector, 
    cp.sector_key 
order by 5 desc;     

