import json
import yfinance as yf
from datetime import datetime
import pandas as pd
import boto3

kinesis = boto3.client('kinesis','us-east-2')
def lambda_handler(event, context):
    # TODO implement
    tickers = ["FB","SHOP","BYND","NFLX","PINS","SQ","TTD","OKTA","SNAP","DDOG"]
    for ticker in tickers:
        symbol = yf.Ticker(ticker)
        hist = symbol.history(period = "1d", interval = "5m", start = "2021-05-11", end = "2021-05-12")
        hist.reset_index(inplace=True)
        hist["name"] = ticker
        hist["high"] = hist["High"]
        hist["low"] = hist["Low"]
        for i in range(len(hist)):
            hist["ts"] = hist["Datetime"].iloc[i].strftime("%Y-%m-%d %I:%M:%S-4:00")
            response = kinesis.put_record(
               StreamName = "sta9760s2021_stream2",
                Data = (hist[["high","low","ts","name"]].iloc[i].to_json() + "\n"),
                PartitionKey = "partitionkey") 
    return {
        'statusCode': 200,
        'body': response
    }
