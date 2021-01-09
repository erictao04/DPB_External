import os
from pathlib import Path
import pandas as pd


class OpenPkl:
    def __init__(self):
        self.open_pkl()

    def open_pkl(self):
        pd.set_option(r"display.max_rows", None, r"display.max_columns", None)
        folder = Path(Path.cwd())

        for filename in os.listdir(folder):
            if not filename.endswith('.pkl'):
                continue

            data_df = pd.read_pickle(folder/filename)
            print(data_df)


OpenPkl()
