CREATE TABLE IF NOT EXISTS company_profiles (
    id TEXT PRIMARY KEY,
    ticker TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    industry TEXT,
    industry_key TEXT,
    sector TEXT,
    sector_key TEXT,
    country TEXT,
    website TEXT,
    market_cap BIGINT,
    employees INTEGER
);

CREATE TABLE IF NOT EXISTS company_historical_data (
    id TEXT,
    date DATE NOT NULL,
    ticker TEXT,
    price FLOAT,
    industry TEXT
);

CREATE TABLE IF NOT EXISTS company_annual_financial_data (
    id SERIAL PRIMARY KEY,
    ticker TEXT REFERENCES company_profiles(ticker),
    year DATE,
    total_revenue FLOAT,
    gross_profit FLOAT,
    net_income FLOAT,
    total_debt FLOAT
);

CREATE TABLE IF NOT EXISTS senators (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    twitter_handle TEXT,
    net_worth FLOAT
);

CREATE TABLE IF NOT EXISTS senator_transactions (
    id SERIAL PRIMARY KEY,
    senator_id INTEGER REFERENCES senators(id),
    ticker TEXT REFERENCES company_profiles(ticker),
    owner TEXT,
    asset_description TEXT,
    asset_type TEXT,
    amount FLOAT
);
