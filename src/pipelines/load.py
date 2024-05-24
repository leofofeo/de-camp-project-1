import yfinance as yf
import pandas as pd

def load_company_profiles(df, engine):
    print("\nLoading data for company_profiles")
    print(df.head(5))
    df.to_sql("company_profiles", con=engine, if_exists="append", index=False)

def load_company_historical_data(df, engine):
    print("\nLoading data for company_historical_data")
    print(df.head(5))
    df.to_sql("company_historical_data", con=engine, if_exists="append", index=False)