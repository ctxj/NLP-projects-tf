#Preprocess news headline and date data, adding labels based on stock's closing difference

#Imports
import pandas as pd
import numpy as np

#Loading data
hl = 'FB_headlines.csv' #From scraper
data = 'FB.csv' #From finance.yahoo.com, daily closing prices

#Function for processing the data
def processing(hl_file, data_file, file_name):
    df_hl = pd.read_csv(hl_file)

    #Adding year for news with dates in 2020
    new_dates = []
    for row in df_hl['Date']:
        year = ', 20'
        add = ', 2020'
        if year in df_hl['Date']:
            new_dates.append(row)
        else:
            new_dates.append(row+add)

    df_hl['Date'] = new_dates
    df_hl['Date'] = pd.to_datetime(df_hl['Date']).dt.strftime('%d/%m/%Y') #Formatting dates to datetime object with the correct format, matching dates from finance.yahoo.com

    df_hl.to_csv(f'{file_name}_processed.csv', index=False)

    df_data = pd.read_csv(data_file)

    #Calculate percentage difference from yesterday's closing price
    df_data['Adj Close'] = df_data['Adj Close'].pct_change()

    # def catergorical_labeler(x):
    #     if x < -0.02:
    #         return 0
    #     elif x >= -0.02 and x <= 0.02:
    #         return 1
    #     else:
    #         return 2

    # df_data['Labels'] = df_data['Adj Close'].apply(catergorical_labeler)
    # df_data.Labels.astype(np.int)

    #Similar function(catergorical_labeler) to the one above, vectorized to speed up function
    #Map labels 0, 1, 2 based on closing price percentage change
    df_data['Labels'] = np.where(df_data['Adj Close'] < -0.02, 0,
                            np.where((df_data['Adj Close'] >= -0.02) & (df_data['Adj Close'] <= 0.02), 1, 2))
    df_data.Labels.astype(np.int)    

    #Drop unnecessary columns
    df_data = df_data.drop(columns=['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
    df_data['Date'] = pd.to_datetime(df_data['Date']).dt.strftime('%d/%m/%Y')

    df_data.to_csv(f'{file_name}_data.csv', index=False)

    #Merge the two dataframes which contains Dates, News headlines and Labels
    df = pd.merge(df_hl, df_data, on='Date')
    df = df.sort_index(ascending=False)

    #Save dataframe into csv
    df.to_csv(f"processed_{file_name}_catergorical.csv", index=False)

#Execute function
processing(hl_file=hl, data_file=data, file_name='FB')