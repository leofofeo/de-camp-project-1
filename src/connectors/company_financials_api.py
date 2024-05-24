import yfinance as yf
import pandas as pd

class CompanyFinancialsAPI:
    def __init__(self, tickers):
        self.tickers = tickers
        self.financial_data = []

    def get_financial_data(self):
        for ticker in self.tickers:
            company = yf.Ticker(ticker)

            income_statement = company.financials.T
            balance_sheet = company.balance_sheet.T

            income_statement = income_statement.reindex(index=income_statement.index.union(balance_sheet.index))
            balance_sheet = balance_sheet.reindex(index=income_statement.index)

            combined_data = pd.DataFrame({
                'Year': income_statement.index,
                'Ticker': ticker,
                'Total Revenue': income_statement['Total Revenue'],
                'Gross Profit': income_statement['Gross Profit'],
                'Net Income': income_statement['Net Income'],
                'Total Debt': balance_sheet['Total Debt']
            })

            self.financial_data.append(combined_data)

        financial_df = pd.concat(self.financial_data)
        financial_df.dropna(inplace=True)
        financial_df.reset_index(drop=True, inplace=True)

        return financial_df
