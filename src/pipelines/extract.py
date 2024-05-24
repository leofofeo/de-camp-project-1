import requests, psycopg2
import yfinance as yf
import pandas as pd
from .load import (
    load_company_profiles, 
    load_company_historical_data,
    load_senator_trades,
    load_company_financials,
)

def extract_data(engine, db_conn_data=None):
    print("Extracting data")

    df = extract_senator_trades()
    load_senator_trades(df, engine)

    tickers = extract_tickers(db_conn_data)
    tickers = tickers[:5]
    df = extract_company_profiles(tickers)
    load_company_profiles(df, engine)

    df = extract_company_historical_data(tickers)
    load_company_historical_data(df, engine)

    # df = extract_company_financials(tickers)
    # load_company_financials(df, engine)

def extract_tickers(db_conn_data):
    print("Extracting tickers")
    query = "SELECT DISTINCT ticker FROM senator_trades"
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
    return [ticker[0] for ticker in tickers[1:]]


def extract_company_profiles(tickers):
    print("Extracting data for company_profiles")
    df = pd.DataFrame()

    for ticker in tickers:
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


def extract_company_historical_data(tickers):
    print("Extracting data for company_historical_data")
    historical_data = []
    year = 2023
    for ticker in tickers:
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


def extract_company_financials(tickers):
    print("Extracting data for company_historical_data")
    financial_data = []

    for ticker in tickers:
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
        
        df = df[allowed_columns]
        df.rename(columns={'senator': 'senator_name'}, inplace=True)
        
        # mask = df['ticker'].str.contains(' ', na=False)
        # df = df[df['ticker'] != 'N/A']
        df['ticker'].replace('N/A', pd.NA, inplace=True)
        df = df.dropna(subset=['ticker'])
        
        return df
    else:
        print(f"Failed to retrieved data: {response.status_code}")
        return pd.DataFrame()
    