import yfinance as yf
import pandas as pd
from .load import load_company_profiles

TICKERS = [
    "AAPL",
    "MSFT",
]

def extract_data(engine):
    print("Extracting data")
    df = extract_company_profiles()
    load_company_profiles(df, engine)

    # TODO: implement the rest of the extract_data function


def extract_company_profiles():
    print("Extracting data for company_profiles")
    df = pd.DataFrame()

    for ticker in TICKERS:
        print("Extracting data for ", ticker)
        stock = yf.Ticker(ticker)
        info = stock.info
    
    # Extract the required information
        stock_info = {
            "id": info.get("uuid", ""),
            "ticker": info.get("symbol", ""),
            "name": info.get("shortName", ""),
            "industry": info.get("industry", ""),
            "industry_key": info.get("industryKey", ""),
            "sector": info.get("sector", ""),
            "sector_key": info.get("sectorKey", ""),
            "country": info.get("country", ""),
            "website": info.get("website", ""),
            "market_cap": info.get("marketCap", ""),
            "employees": info.get("fullTimeEmployees", "")
        }

        stock_info_df = pd.DataFrame([stock_info])
        df = pd.concat([df, stock_info_df], ignore_index=True)
    
    return df