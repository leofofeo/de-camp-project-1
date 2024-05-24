import yfinance as yf
import pandas as pd

class CompanyProfileAPI:
    def __init__(self, tickers):
        self.tickers = tickers
        self.company_profiles = []

    def get_company_profile(self):
        for ticker in self.tickers:
            company = yf.Ticker(ticker)
            info = company.info
            
            # Extract relevant profile information
            profile = {
                'Ticker': ticker,
                'Name': info.get('shortName'),
                'Industry': info.get('industry'),
                'Sector': info.get('sector'),
                'Country': info.get('country'),
                'Business Summary': info.get('longBusinessSummary'),
                'Website': info.get('website'),
                'Market Cap': info.get('marketCap'),
                'Employees': info.get('fullTimeEmployees')
            }
            
            self.company_profiles.append(profile)

        company_profile_df = pd.DataFrame(self.company_profiles)
        company_profile_df.reset_index(drop=True, inplace=True)

        return company_profile_df
