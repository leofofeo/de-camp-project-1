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
