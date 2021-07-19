import json
import pandas as pd
import numpy as np
from yahoo_fin import stock_info
from multiprocessing import Pool
import datetime
from collections import Counter


end_date = datetime.datetime.now().date()
start_date = end_date - datetime.timedelta(days=365 * 2)

def get_historical_data(ticker, start_date=start_date, end_date=end_date):
    try:
        headers = headers = {'User-Agent': ''}
        return stock_info.get_data(
            ticker, start_date=start_date, end_date=end_date, index_as_date = False, interval="1d", headers=headers)
    except:
        # really don't do this, it's hacky but whatever
        return ('ERROR', ticker)

if __name__ == '__main__':
    historical_data = []
    with Pool(32) as p:
        historical_data = p.map(get_historical_data, ['amzn', 'aapl'])

