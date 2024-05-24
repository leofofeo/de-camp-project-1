import yfinance as yf
import pandas as pd

class TickerHist:
    def __init__(self, start_date, end_date, tickers):
        self.start_date = start_date
        self.end_date = end_date
        self.tickers = tickers
        self.data_frames = []

    def GettickerHist(self):
        for ticker in self.tickers:
            ticker_data = yf.Ticker(ticker).history(start=self.start_date, end=self.end_date)
            ticker_data['Ticker'] = ticker
            self.data_frames.append(ticker_data)
        self.ticker_data_df = pd.concat(self.data_frames)
        self.ticker_data_df.reset_index(drop=True, inplace=True)
        self.ticker_data_df.dropna(inplace=True)
        return self.ticker_data_df
