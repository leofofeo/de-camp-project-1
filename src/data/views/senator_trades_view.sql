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

