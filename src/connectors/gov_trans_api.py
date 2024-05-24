
import pandas as pd

class SenateTransactions:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_transactions(self):
        try:
            transactions_df = pd.read_csv(self.file_path)
            return transactions_df
        except Exception as e:
            print(f"Error loading transactions: {e}")
            return None