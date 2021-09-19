import json
import pandas as pd
import numpy as np
from yahoo_fin import stock_info
from multiprocessing import Pool
import datetime
from collections import Counter
import requests


def get_data(ticker, start_date = None, end_date = None, index_as_date = True,
             interval = "1d", headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
):
    '''Downloads historical stock price data into a pandas data frame.  Interval
       must be "1d", "1wk", "1mo", or "1m" for daily, weekly, monthly, or minute data.
       Intraday minute data is limited to 7 days.
    
       @param: ticker
       @param: start_date = None
       @param: end_date = None
       @param: index_as_date = True
       @param: interval = "1d"
    '''

    if interval not in ("1d", "1wk", "1mo", "1m"):
        raise AssertionError("interval must be of of '1d', '1wk', '1mo', or '1m'")


    # build and connect to URL
    site, params = stock_info.build_url(ticker, start_date, end_date, interval)
    resp = requests.get(site, params = params, headers = headers)


    if not resp.ok:
        raise AssertionError(resp.json())


    # get JSON response
    data = resp.json()

    # get open / high / low / close data
    frame = pd.DataFrame(data["chart"]["result"][0]["indicators"]["quote"][0])

    # get the date info
    temp_time = data["chart"]["result"][0]["timestamp"]

    if interval != "1m":

        # add in adjclose
        frame["adjclose"] = data["chart"]["result"][0]["indicators"]["adjclose"][0]["adjclose"]
        frame.index = pd.to_datetime(temp_time, unit = "s")
        frame.index = frame.index.map(lambda dt: dt.floor("d"))
        frame = frame[["open", "high", "low", "close", "adjclose", "volume"]]

    else:

        frame.index = pd.to_datetime(temp_time, unit = "s")
        frame = frame[["open", "high", "low", "close", "volume"]]


    frame['ticker'] = ticker.upper()

    if not index_as_date:
        frame = frame.reset_index()
        frame.rename(columns = {"index": "date"}, inplace = True)

    return frame

stock_info.get_data = get_data


end_date = datetime.datetime.now().date()
start_date = end_date - datetime.timedelta(days=365 * 2)

def get_historical_data(ticker, start_date=start_date, end_date=end_date):
    headers = headers = {'User-Agent': ''}
    return stock_info.get_data(
        ticker, start_date=start_date, end_date=end_date, index_as_date = False, interval="1d", headers=headers)

if __name__ == '__main__':
    historical_data = []
    with Pool(32) as p:
        historical_data = p.map(get_historical_data, ['amzn', 'aapl'])

