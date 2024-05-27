
/*
view top_senator_gains_from_purchases provides view of senators who benefited the most from purchases (greater than 4)
*/

CREATE OR REPLACE VIEW top_senator_gains_from_purchases AS
SELECT 
   *
FROM 
    senator_trades_view cv
WHERE 
    cv.tran_type = 'Purchase' and percentage_increase is not null
  AND percentage_increase >4
ORDER BY 1;