import sys
import os

import pytest
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

@pytest.fixture
def senator_trades_response():
    return [
        {
            "transaction_date": "04/18/2023",
            "owner": "Spouse",
            "ticker": "ESS",
            "asset_description": "Essex Property Trust, Inc. Common Stock",
            "asset_type": "Stock",
            "type": "Sale (Full)",
            "amount": "$1,001 - $15,000",
            "comment": "--",
            "party": "Democrat",
            "state": "RI",
            "industry": "Real Estate Investment Trusts",
            "sector": "Consumer Services",
            "senator": "Sheldon Whitehouse",
            "ptr_link": "https://efdsearch.senate.gov/search/view/ptr/9fc025a0-f893-47b2-9252-a2820737a409/",
            "disclosure_date": "05/17/2023"
        },
        {
            "transaction_date": "04/18/2023",
            "owner": "Self",
            "ticker": "ESS",
            "asset_description": "Essex Property Trust, Inc. Common Stock",
            "asset_type": "Stock",
            "type": "Sale (Full)",
            "amount": "$1,001 - $15,000",
            "comment": "--",
            "party": "Democrat",
            "state": "RI",
            "industry": "Real Estate Investment Trusts",
            "sector": "Consumer Services",
            "senator": "Sheldon Whitehouse",
            "ptr_link": "https://efdsearch.senate.gov/search/view/ptr/9fc025a0-f893-47b2-9252-a2820737a409/",
            "disclosure_date": "05/17/2023"
        },
        {
            "transaction_date": "05/16/2023",
            "disclosure_date": "05/16/2023",
            "owner": "N/A",
            "ticker": "N/A",
            "asset_description": "This filing was disclosed via scanned PDF. Use link in ptr_link column to view the PDF.",
            "asset_type": "PDF Disclosed Filing",
            "type": "N/A",
            "amount": "Unknown",
            "comment": "",
            "senator": "Michael F. Bennet",
            "ptr_link": "https://efdsearch.senate.gov/search/view/ptr/f590a331-1f74-4d08-b79f-88930593f314/"
        }
    ]

@pytest.fixture
def senator_trades_df(senator_trades_response):
    df = pd.DataFrame(senator_trades_response)
    df = df[['senator', 'ticker', 'owner', 'asset_description', 'asset_type', 'amount', 'transaction_date', 'disclosure_date', 'type']]
    df.rename(columns={'senator': 'senator_name'}, inplace=True)
    return df