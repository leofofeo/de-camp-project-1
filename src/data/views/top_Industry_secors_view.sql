CREATE OR REPLACE VIEW top_industries_view AS
SELECT 
    cp.industry, 
    cp.industry_key, 
    cp.sector, 
    cp.sector_key, 
    SUM(cp.market_cap)
    --AVG(chd.price) AS avg_price, 
   -- MIN(chd.price) AS min_price, 
    --MAX(chd.price) AS max_price
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
order by 5 desc     