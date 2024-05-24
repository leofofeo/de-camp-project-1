CREATE TABLE company_profile (
    id SERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL,
    name VARCHAR(255),
    industry VARCHAR(255),
    sector VARCHAR(255),
    country VARCHAR(100),
    business_summary TEXT,
    website VARCHAR(255),
    market_cap BIGINT,
    employees INTEGER,
    CONSTRAINT unique_ticker UNIQUE (ticker)
);
