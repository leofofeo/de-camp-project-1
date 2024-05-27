

/*
view top_senator_losses_from_sales provides view of senators who incurred greater than 10% losses from sales
*/

CREATE OR REPLACE VIEW top_senator_losses_from_sales AS
SELECT 
   *
FROM 
    senator_trades_view cv
WHERE 
    cv.tran_type like '%Sale%' and percentage_decrease is not null
  AND percentage_decrease < -10
ORDER BY 1;
