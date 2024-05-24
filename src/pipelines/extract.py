import yfinance as yf
import pandas as pd
from .load import load_company_profiles, load_company_historical_data
from data.tickers import TICKERS

def extract_data(engine):
    print("Extracting data")

    # df = extract_company_profiles()
    # load_company_profiles(df, engine)

    df = extract_company_historical_data()
    load_company_historical_data(df, engine)

    # TODO; create senator table
    
    # TODO: implement extract senator trades


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
            "ticker": info.get("symbol", None),
            "name": info.get("shortName", None),
            "industry": info.get("industry", None),
            "industry_key": info.get("industryKey", None),
            "sector": info.get("sector", None),
            "sector_key": info.get("sectorKey", None),
            "country": info.get("country", None),
            "website": info.get("website", None),
            "market_cap": info.get("marketCap", None),
            "employees": info.get("fullTimeEmployees", None)
        }

        stock_info_df = pd.DataFrame([stock_info])
        df = pd.concat([df, stock_info_df], ignore_index=True)
    
    return df


def extract_company_historical_data():
    print("Extracting data for company_historical_data")
    historical_data = []
    year = 2023
    for ticker in TICKERS[0:25]:
        stock = yf.Ticker(ticker)
        info = stock.info
        start_date = f"{year}-12-1"
        end_date = f"{year}-12-31"
        try:
            hist = stock.history(start=start_date, end=end_date)
            for index, row in hist.iterrows():
                data = {
                    "id": info.get("uuid", ""),
                    "date": index.date(),
                    "ticker": ticker,
                    "price": row['Close'],
                    "industry": info.get("industry", "")
                }
                historical_data.append(data)
        except Exception as e:
            print(f"Error extracting data for {ticker}: {e}")
            continue
    return pd.DataFrame(historical_data)