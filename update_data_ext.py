import os
import re
from pathlib import Path
from convert_to_ohlc_ext import TradingViewData


class UpdateStockData:
    def __init__(self, timeframe):
        self.timeframe = timeframe
        os.makedirs(self.timeframe, exist_ok=True)

    def search_current_data(self):
        current_data_path = Path(Path.cwd())/self.timeframe
        self.data_filenames = []
        pkl_data_regex = re.compile(r'(([A-Z]+)_(\d+([a-zA-Z])?))')

        for filename in os.listdir(current_data_path):

            stock_element = pkl_data_regex.search(filename)

            if not stock_element:
                continue

            ticker_tf = stock_element.group(1)

            if ticker_tf not in self.data_filenames:
                self.data_filenames.append(ticker_tf)

    def search_downloads(self):
        download_path = Path(Path.cwd())/'Raw_Data'

        raw_data_regex = re.compile(r'''
        BATS_
        ([A-Z]+),  # Ticker
        \s(\d+([a-zA-Z]+)?)  # Time Frame
        (\s\(\d\))?
        .csv
        ''', re.VERBOSE)

        for filename in os.listdir(download_path):

            stock_element = raw_data_regex.search(filename)

            if not stock_element:
                continue

            ticker = stock_element.group(1)
            timeframe = stock_element.group(2)
            ticker_tf = f'{ticker}_{timeframe}'

            if ticker_tf not in self.data_filenames:
                if timeframe == self.timeframe:
                    stock_data = TradingViewData(ticker, timeframe)
                    stock_data.latest_download()
                    stock_data.read_raw_csv()
                    stock_data.to_pickle()

    def update(self):
        self.search_current_data()
        self.search_downloads()
