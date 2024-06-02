import yfinance as yf
import pandas as pd

from logger import logger

def load_company_profiles(df, engine):
    logger.info("\nLoading data for company_profiles")
    logger.info(df.head(5))
    df.to_sql("company_profiles", con=engine, if_exists="append", index=False)

def load_company_historical_data(df, engine):
    logger.info("\nLoading data for company_historical_data")
    logger.info(df.head(5))
    df.to_sql("company_historical_data", con=engine, if_exists="append", index=False)


def load_senator_trades(df, engine):
    logger.info("\nLoading data for senator_trades")
    logger.info(df.head(5))
    df.to_sql("senator_trades", con=engine, if_exists="append", index=False)

def load_company_financials(df, engine):
    logger.info("\nLoading data for company_annual_financial_data")
    logger.info(df.head(5))
    df.to_sql("company_annual_financial_data", con=engine, if_exists="append", index=False)