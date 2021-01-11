# Double Point Breakout Strategy Backtester
# This program is not financial advice. Results are derived from the program are simply an analysis of the past based on a specific theory.

## Table of content
* [General Info](#general-info)
* [Strategy Overview](#strategy-overview)
* [Technologies](#technologies)
* [Set up](#setup)

## General Info
### Description of Initial Folders and Files
#### DPB_Strategy_External.py
  * Only program you need to run
  * Uses all the files and folders below
#### Raw_Data
  * Folder of CSV files of stock data
#### common_functions_ext.py
  * Contains functions I regularly use in numerous projects
#### convert_to_ohlc_ext.py
  * Converts CSV file to pandas dataframe before saving it in a pickle file in 1D
#### create_batch.py
  * Creates batch file in Results and Stats folder
#### get_earnings_ext.py
  * Scrapes earnings from Yahoo Finance
#### open_pkl.py
  * Script ran by batch file created in Results and Stats folder to display Pandas Dataframe
#### update_data_ext.py
  * Loops through new folder of CSV data and converts the new ones into Pandas Dataframe

### Description of Folders Created After DPB_Strategy_External.py Runs
#### 1D
  * Folder of pickle files
  * Converted each stock data's CSV file to Pandas Dataframe
#### Results
  * Folder of tables of main statistics of the analysis
  * 1d_hld.xlsx
    * Excel file of the results of the analysis
  * 1d_hld.pkl
    * Pickle file of Pandas dataframe of the results of the analysis
  * read_pkl.bat
    * Opens pickle file in command prompt
#### Stats
  * Folder of tables of less important statistic of the analysis
  * 1d_hld.xlsx
    * Excel file of the results of the analysis
  * 1d_hld.pkl
    * Pickle file of Pandas dataframe of the results of the analysis
  * read_pkl.bat
    * Opens pickle file in command prompt

## Strategy Overview
### Strategy Theory (not neccessarily right)
* Stocks have greater growth potential after a large decline
* Resistance levels dictate on when to sell and if to enter
### Entry Criteria (all number criterias can be modified in DPB_Strategy_External.py without modifying the class)
#### Entry Signal
* Stock must have already declined minimum 20% from recent high
* Daily price must close above potential entry point
* Close must be closer from resistance line below than resistance line above
* Open on following day (entry day) must open minimum .5% below resistance line below
* Entry must be more than 4 days from an earnings release
* Entry date must be less than 6 months from first high of entry point
#### Entry Point
* Entry preceded by 2 highs
* Highs must be minimum 7 days apart
* First of two highs must be higher
* High prices must be a maximum of 2% apart
#### Resistance Lines
* Initial resistance line starts at high before 20% decline
* Ensuing resistance line maximum 9% below previous resistance
* Ensuing resistance line minimum 8% below previous resistance
* Lines drawn based on past price movements
#### Stop Loss
* 2% stop loss below entry point
* Or .5% stop loss below resistance line below
* Whichever happens first
#### Take Profit
* Sell day before earnings release
* Sell following day if difference from day's high to close is more than 1% and the high was greater than 1.5% below resistance line above

## Technologies
* pandas_datareader version: 0.9.0
* openpyxl version: 2.6.2
* requests version: 2.24.0
* bs4 version: 0.0.1
* matplotlib version: 3.3.2
* pandas version: 1.1.4
* numpy version: 1.19.4
* re version: 2.2.1
* datetime version: auto
* pathlib version: auto
* copy version: auto
* os version: auto
* threading version: auto
* time version: auto
* itertools version: auto 


## Setup
* Install all files and folders from this remote repository
* DO NOT change location or names of files (or it will break)
* To run the program, open DPB_Strategy_External.py and run it in your code editor
* Program will automatically create folders and files
* Check results by opening the excel files or batch files that displays a pandas dataframe of results
