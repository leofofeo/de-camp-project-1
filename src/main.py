from dotenv import load_dotenv
import os
import yaml
from pathlib import Path
from sqlalchemy import Table, MetaData, Column, Integer, String, Float

from connectors.ticker_hist_api import TickerHist
from assets.ticker_hist_transform import DataTransformer
from connectors.company_financials_api import CompanyFinancialsAPI
from connectors.company_profile_api import CompanyProfileAPI
from connectors.gov_trans_api import SenateTransactions
from load.financials_loader import LoadData

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == '__main__':
    
    load_dotenv()

    SERVER_NAME = os.environ.get("SERVER_NAME")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    PORT = os.environ.get("PORT")

    db_url = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{SERVER_NAME}:{PORT}/{DATABASE_NAME}'
    
    base_dir = Path(__file__).resolve().parent
    config_file = base_dir / 'config' / 'ticker.yaml'

    config = load_config(config_file)
    
    start_date   = config.get("start_date")
    end_date     = config.get("end_date")
    ticker_list  = config.get('ticker_list')
    senate_trans_reference_path = config.get('senate_trans_reference_path')


    tickers = TickerHist(start_date, end_date, ticker_list)
    ticker_hist_df = tickers.GettickerHist()

    transformer = DataTransformer()
    ticker_hist_df = transformer.transform(ticker_hist_df)

    financials = CompanyFinancialsAPI(ticker_list)
    company_annual_financials_df = financials.get_financial_data()

    profiles = CompanyProfileAPI(ticker_list)
    company_profile_data_df = profiles.get_company_profile()

    print("loading data....")

    senate_transactions_df = SenateTransactions(senate_trans_reference_path)
    senate_transactions_df = senate_transactions_df.load_transactions()

    loader = LoadData(db_url)
    loader.load_dataframes(ticker_hist_df, company_annual_financials_df, company_profile_data_df, senate_transactions_df)

    print("loading complete....")
