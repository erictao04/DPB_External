# convert_to_ohlc.py - External use version of original
import pandas as pd
import itertools
from pathlib import Path
import os


class TradingViewData:
    '''
    Converts downloaded TradingView data csv into pandas dataframe

        Stores converted dataframe in pickle file
    '''

    def __init__(self, ticker, tf, same_folder=False):
        self.ticker = ticker.upper()
        self.tf = tf.upper()
        self.new_filename = f"{self.ticker}_{tf}.pkl"
        os.makedirs(self.tf, exist_ok=True)

        if not same_folder:
            self.download_dir = Path('C:\\')/'Users'/'User'/'Downloads'
            self.filename = f"BATS_{self.ticker}, {self.tf}.csv"
            self.data_path = self.download_dir/self.filename
        else:
            self.download_dir = Path(Path.cwd())/"Raw_Data"
            self.filename = f"BATS_{self.ticker}, {self.tf}.csv"
            self.data_path = self.download_dir/self.filename

        self.new_file_path = Path(Path.cwd())/tf/self.new_filename

    def latest_download(self, use_latest=True):
        '''
        Ensures the use of latest downloaded file (not use_latest)

            Function tries to open potential files and uses the one
            with the highest number in brackets(latest) if multiple
            csv of a stock is stored in computer
        '''
        if use_latest:
            for i in itertools.count(start=1):
                pot_path = f"{str(self.data_path)[:-4]} ({i}).csv"
                if not os.path.exists(pot_path):
                    if i > 1:
                        self.filename = f"{self.filename[:-4]} ({i-1}).csv"
                        self.data_path = self.download_dir/self.filename
                    break

    def read_raw_csv(self):
        '''
        Converts csv into pandas dataframe, renames each columns
        accordingly and adds all dates to list for later  use

        '''
        self.data = pd.read_csv(self.data_path)
        self.data.columns = ["Date", "Open", "High", "Low", "Close", "", ""]
        self.lst_new_dt = []

        for (_, a_dt, *_) in self.data.itertuples():
            self.lst_new_dt.append(a_dt[:10])

    def to_pickle(self):
        '''
        Converts all stringed dates to real dates, sets them as
        the dataframe's index and saves dataframe of dates, open,
        high, low and close to a pickle file

        '''
        self.data.index = pd.to_datetime(self.lst_new_dt)
        self.data = self.data[["Open", "High", "Low", "Close"]]

        os.makedirs(Path(self.tf), exist_ok=True)
        self.data.to_pickle(self.new_file_path)
