ALTER TABLE senator_trades
    ADD COLUMN min_transaction_amount INTEGER,
    ADD COLUMN max_transaction_amount INTEGER;

UPDATE senator_trades
SET
    min_transaction_amount = CASE
        WHEN amount = 'Unknown' THEN NULL
        ELSE CAST(REGEXP_REPLACE(SPLIT_PART(amount, '-', 1), '[^\d]', '', 'g') AS INTEGER)
    END,
    max_transaction_amount = CASE
        WHEN amount = 'Unknown' THEN NULL
        ELSE CAST(REGEXP_REPLACE(SPLIT_PART(amount, '-', 2), '[^\d]', '', 'g') AS INTEGER)
    END;