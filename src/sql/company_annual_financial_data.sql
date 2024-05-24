CREATE TABLE company_annual_financial_data (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    year INTEGER NOT NULL,
    total_revenue NUMERIC,
    gross_profit NUMERIC,
    net_income NUMERIC,
    total_debt NUMERIC,
    CONSTRAINT unique_ticker_year UNIQUE (ticker, year)
);