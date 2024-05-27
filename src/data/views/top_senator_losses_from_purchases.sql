

/*
view top_senator_losses_from_purchases provides view of senators who incurred greater than 5% losses from purchases
*/

CREATE OR REPLACE VIEW top_senator_losses_from_purchases AS
SELECT 
   *
FROM 
    senator_trades_view cv
WHERE 
    cv.tran_type = 'Purchase' and percentage_decrease is not null
  AND percentage_decrease < -5
ORDER BY     percentage_increase  DESC, senator_name asc, transaction_date asc;

