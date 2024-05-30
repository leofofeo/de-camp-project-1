import requests, psycopg2, os
import yfinance as yf
import pandas as pd
from .load import (
    load_company_profiles, 
    load_company_historical_data,
    load_senator_trades,
    load_company_financials,
)
from dotenv import load_dotenv

def extract_data(engine, db_conn_data=None):
    print("Extracting data")

    df = extract_senator_trades()
    load_senator_trades(df, engine)

    tickers = extract_tickers(db_conn_data)[1:]
    
    df = extract_company_profiles(tickers)
    load_company_profiles(df, engine)

    df = extract_company_historical_data(tickers)
    load_company_historical_data(df, engine)

    df = extract_company_financials(tickers)
    load_company_financials(df, engine)

def extract_tickers(db_conn_data):
    print("Extracting tickers")
    
    """
    These are the top 20 tickers ('AAPL','MSFT','BAC','DIS','NFLX', 'PFE','DISCA','T','FEYE','FDC','URBN','CZR','NVDA','AMZN','PYPL','FB','WFC','GE','CLF','INTC')
    replace the tickers query above with the below sample query to limit the runtime and start testing the incremental datasets...
    """
    load_dotenv()

    run_environment = os.getenv("RUN_ENV")
    query = "SELECT DISTINCT ticker FROM senator_trades"

    if run_environment == "TESTING":
        query = "SELECT DISTINCT ticker FROM senator_trades where ticker in ('AAPL','MSFT','BAC','DIS','NFLX')"
    elif run_environment == "INCREMENTAL_TESTING_1":
        query = "SELECT DISTINCT ticker FROM senator_trades where ticker in ('AAPL', 'MSFT')" 
    elif run_environment == "INCREMENTAL_TESTING_2":
        query = "SELECT DISTINCT ticker FROM senator_trades where ticker in ('BAC','NVDA','AMZN','PYPL')" 
    
    conn = psycopg2.connect(
        dbname=db_conn_data["db_name"],
        user=db_conn_data["db_user"],
        password=db_conn_data["db_password"],
        host=db_conn_data["db_host"],
        port=db_conn_data["db_port"]
    )
    cur = conn.cursor()
    cur.execute(query)
    tickers = cur.fetchall()
    cur.close()
    conn.close()
    print(tickers)
    return [ticker[0] for ticker in tickers if ticker[0] not in [None, 'N/A']]


def extract_company_profiles(tickers):
    print("Extracting data for company_profiles")
    
    # Use yf.Tickers to fetch data for multiple tickers at once
    stocks = yf.Tickers(tickers)
    profiles_data = []

    for ticker in tickers:
        print("Extracting data for", ticker)
        try:
            stock = stocks.tickers[ticker]
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

            profiles_data.append(stock_info)
        except Exception as e:
            print("Error extracting data for", ticker, ":", e)
            continue

    return pd.DataFrame(profiles_data)

def extract_company_historical_data(tickers):
    print("Extracting data for company_historical_data")

    historical_data = []
    year = 2023
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    
    stocks = yf.Tickers(tickers)
    
    for ticker in tickers:
        try:
            stock = stocks.tickers[ticker]
            info = stock.info
            hist = stock.history(start=start_date, end=end_date)

            # Calculate the price moving average 
            hist['dma_10'] = hist['Close'].rolling(window=10, min_periods=1).mean()
            hist['dma_30'] = hist['Close'].rolling(window=30, min_periods=1).mean()
            hist['dma_60'] = hist['Close'].rolling(window=60, min_periods=1).mean()
            
            for index, row in hist.iterrows():
                data = {
                    "id": info.get("uuid", None),
                    "date": index.date(),
                    "ticker": ticker,
                    "price": row['Close'],
                    "industry": info.get("industry", None),
                    "dma_10": row['dma_10'],
                    "dma_30": row['dma_30'],
                    "dma_60": row['dma_60']
                }
                historical_data.append(data)
        except Exception as e:
            print(f"Error extracting data for {ticker}: {e}")
            continue
    return pd.DataFrame(historical_data)


def extract_company_financials(tickers):
    print("Extracting data for company_financials")
    financial_data = []
    
    year = 2023
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    # Use yf.Tickers to fetch data for multiple tickers at once
    stocks = yf.Tickers(tickers)

    for ticker in tickers:
        print("Extracting data for", ticker)
        
        try:
            company = stocks.tickers[ticker]

            financials = company.financials.T  
            balance_sheet = company.balance_sheet.T  

            if not financials.index.equals(balance_sheet.index):
                all_years = financials.index.union(balance_sheet.index)
                financials = financials.reindex(all_years)
                balance_sheet = balance_sheet.reindex(all_years)

            combined_df = pd.concat([financials, balance_sheet], axis=1)

            combined_df = combined_df.loc[start_date:end_date]  # Filter by date range

            combined_data = pd.DataFrame({
                'year': combined_df.index,
                'ticker': ticker,
                'total_revenue': combined_df.get('Total Revenue'),
                'gross_profit': combined_df.get('Gross Profit'),
                'net_income': combined_df.get('Net Income'),
                'total_debt': combined_df.get('Total Debt')
            })

            financial_data.append(combined_data)
        
        except Exception as e:
            print(f"Error extracting data for {ticker}: {e}")
            continue

    return pd.concat(financial_data, ignore_index=True)

def extract_senator_trades():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.json"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()

        df = pd.json_normalize(json_data)
        allowed_columns = ['senator', 'ticker', 'owner', 'asset_description', 'asset_type', 'amount', 'transaction_date', 'disclosure_date', 'type']
        
        df = df[allowed_columns]
        df.rename(columns={'senator': 'senator_name'}, inplace=True)
        
        df['ticker'].replace('N/A', pd.NA, inplace=True)
        df = df.dropna(subset=['ticker'])
        
        return df
    else:
        print(f"Failed to retrieved data: {response.status_code}")
        return pd.DataFrame()
    