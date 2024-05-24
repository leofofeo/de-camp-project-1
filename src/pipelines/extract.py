import requests
import yfinance as yf
import pandas as pd
from .load import (
    load_company_profiles, 
    load_company_historical_data,
    load_senator_trades,
    load_company_financials,
)
from data.tickers import TICKERS

def extract_data(engine):
    print("Extracting data")

    # df = extract_company_profiles()
    # load_company_profiles(df, engine)

    # df = extract_company_historical_data()
    # load_company_historical_data(df, engine)

    # df = extract_senator_trades()
    # load_senator_trades(df, engine)

    df = extract_company_financials()
    load_company_financials(df, engine)


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
    for ticker in TICKERS:
        stock = yf.Ticker(ticker)
        info = stock.info
        start_date = f"{year}-1-1"
        end_date = f"{year}-12-31"
        try:
            hist = stock.history(start=start_date, end=end_date)
            for index, row in hist.iterrows():
                data = {
                    "id": info.get("uuid", None),
                    "date": index.date(),
                    "ticker": ticker,
                    "price": row['Close'],
                    "industry": info.get("industry", None)
                }
                historical_data.append(data)
        except Exception as e:
            print(f"Error extracting data for {ticker}: {e}")
            continue
    return pd.DataFrame(historical_data)


def extract_company_financials():
    print("Extracting data for company_historical_data")
    financial_data = []

    for ticker in TICKERS:
        print("extracting data for ", ticker)
        company = yf.Ticker(ticker)

        financials = company.financials.T  
        balance_sheet = company.balance_sheet.T  
        
        financials = financials.reindex(index=financials.index.union(balance_sheet.index))
        balance_sheet = balance_sheet.reindex(index=financials.index)
        combined_df = pd.concat([financials, balance_sheet], axis=1)
    
        combined_data = pd.DataFrame({
            'year': combined_df.index,
            'ticker': ticker,
            'total_revenue': combined_df['Total Revenue'],
            'gross_profit': combined_df['Gross Profit'],
            'net_income': combined_df['Net Income'],
            'total_debt': combined_df['Total Debt']
        })
        financial_data.append(combined_data)

    return pd.DataFrame(financial_data)


def extract_senator_trades():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

        df = pd.json_normalize(json_data)
        allowed_columns = ['senator', 'ticker', 'owner', 'asset_description', 'asset_type', 'amount']
        
        # clean up dataframe and match it to the database schema
        df = df[allowed_columns]
        df.rename(columns={'senator': 'senator_name'}, inplace=True)
        print("df has been renamed")
        # df.astype({'amount': 'str'}, copy=False)
        return df
    else:
        print(f"Failed to retrieved data: {response.status_code}")
        return pd.DataFrame()
    