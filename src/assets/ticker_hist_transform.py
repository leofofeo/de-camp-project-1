

class DataTransformer:
    def transform(self, tickers_df):
        # Drop rows with any NaN values
        tickers_df.dropna(inplace=True)
        
        tickers_df['SMA_10'] = tickers_df['Close'].rolling(window=10).mean()
        tickers_df['SMA_30']= tickers_df['Close'].rolling(window=30).mean()
        tickers_df['SMA_50']= tickers_df['Close'].rolling(window=50).mean()
        
        return tickers_df