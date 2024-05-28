
/*
view top_senator_gains_from_sales provides view of senators who benefited the most from sales (greater than 7%)
*/

CREATE OR REPLACE VIEW top_senator_gains_from_sales AS
SELECT 
   *
FROM 
    senator_trades_view cv
WHERE 
    cv.tran_type like '%Sale%' and percentage_increase is not null
  AND percentage_increase > 7
ORDER BY 1;
