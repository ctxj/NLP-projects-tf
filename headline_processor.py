#Download 10 years historical data of stocks from yahoo finance wrapper by 'https://github.com/ranaroussi/yfinance'
#Process historical data for "adj close" prices and find percentage change
#Headline news data from 'https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests?select=analyst_ratings_processed.csv'
#Map price percentage change to date and stock for headline news

#Imports
import concurrent.futures
import pandas as pd
import numpy as np
import yfinance as yf #Yahoo Finance wrapper
from tqdm.auto import tqdm

#Load headline data
df_hl = pd.read_csv('analyst_ratings_processed.csv')
stocks = df_hl['stock']
stocks.dropna(inplace=True)

#Convert tickers of headline news into list
tickers = stocks.unique().tolist()

#Download 10 years of historical prices from yahoo finance
data = yf.download(tickers, period='10y')

df = data.loc[:, ('Adj Close')]
tickers = df.columns.values.tolist() #Clean stocks tickers list, some stocks have been delisted

df.fillna(method='ffill', inplace=True)
df = df.pct_change() #Store adj close prices percentage change into new dataframe

#Format dates to match 
df_hl['date'] = df_hl['date'].str.split(' ', expand=True)[0]
df_hl['date'] = pd.to_datetime(df_hl['date'], errors ='coerce')
df_hl['date'] = df_hl['date'].dt.date

df['date'] = pd.to_datetime(df.index)
df['date'] = df['date'].dt.date

labels = pd.DataFrame()


# for ticker in tqdm(tickers):
#     task = df_hl[df_hl['stock'] == ticker]
#     task2 = pd.merge(task, df[[ticker, 'date']], on='date')
#     task2['label'] = task2[ticker]
#     del task2[ticker]
#     labels = labels.append(task2)

#parallel processing to speed up for loop(same as loop above)
#Match the dates and map percentage price change to headline news
def process_data(ticker):
    task = df_hl[df_hl['stock'] == ticker]
    task2 = pd.merge(task, df[[ticker, 'date']], on='date')
    task2['label'] = task2[ticker]
    del task2[ticker]
    return task2

labels = pd.DataFrame()
pbar = tqdm(total=len(tickers))
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for r in executor.map(process_data, tickers):
            labels = labels.append(r)
            pbar.update(1)
    pbar.close()


labels['label'].replace(0, np.nan, inplace=True)
headlines = labels.dropna()

#Label negative price change as 0 and positive change a 1
headlines['label'] = np.where(headlines['label'] < 0, 0, 1)

headlines.drop(columns=['Unnamed: 0'], inplace=True)

#Save to csv
headlines.to_csv('headlines_labeleds.csv', index=False)
