import pandas as pd
from sqlalchemy import create_engine, inspect

class LoadData:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def load_dataframe(self, data_frame, table_name):
        """
        Loads the DataFrame into the specified PostgreSQL table.
        """
        with self.engine.connect() as conn:
            # Check if table exists
            if not inspect(self.engine).has_table(table_name):
                data_frame.to_sql(table_name, conn, if_exists='replace', index=False)
            else:
                data_frame.to_sql(table_name, conn, if_exists='append', index=False)

    def load_dataframes(self, ticker_df, financial_df, profile_df, senate_trans_df):
        self.load_dataframe(ticker_df, 'ticker_price_hist')
        self.load_dataframe(financial_df, 'annual_financial_data')
        self.load_dataframe(profile_df, 'company_profile')
        self.load_dataframe(senate_trans_df, 'senate_official_trans')


