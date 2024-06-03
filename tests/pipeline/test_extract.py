import pandas as pd

from src.pipelines.extract import extract_senator_trades


def test_extract_senator_trades(mocker, senator_trades_response, senator_trades_df):
    mock_response = mocker.Mock()
    mock_response.json.return_value = senator_trades_response
    mock_response.status_code = 200
    mocker.patch("requests.get", return_value=mock_response)

    result = extract_senator_trades()
    
    for idx, row in result.iterrows():
        for col in senator_trades_df.columns:
            assert row[col] == senator_trades_df.loc[idx, col]