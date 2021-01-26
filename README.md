# Financial News Headlines Sentiment Analysis
Collect financial news headlines by scraping [seekingalpha.com](https://seekingalpha.com/)  
Perform sentiment analysis on headline news using NLP models  
Train models on larger dataset to improve accuracy

## Prerequisites
Python 3.8.6  
[Python libraries](https://github.com/ctxj/NLP-projects-tf/blob/main/requirements.txt) pip install -r requirements.txt  
[Google Chrome driver](https://chromedriver.chromium.org/downloads)

## Data
[Facebook's historical price data](https://github.com/ctxj/NLP-projects-tf/blob/main/FB.csv) From Yahoo finance  
[Web scraper for headline news](https://github.com/ctxj/NLP-projects-tf/blob/main/scaper.py)  
[Processed news headlines](https://github.com/ctxj/NLP-projects-tf/blob/main/processed_FB_catergorical.csv)  
[1 million finance news headlines](https://www.kaggle.com/miguelaenlle/massive-stock-news-analysis-db-for-nlpbacktests?select=analyst_ratings_processed.csv) From kaggle  
[Precessed news headlines(large)](https://github.com/ctxj/NLP-projects-tf/blob/main/headline_processor.py)

## Models
[BiLSTM (trained on large dataset)](https://github.com/ctxj/NLP-projects-tf/blob/main/NLP_BiLSTM_colab.ipynb) - 60% accuracy  
[BERT](https://github.com/ctxj/NLP-projects-tf/blob/main/BERT.ipynb) - 52% accuracy  
[BiLSTM](https://github.com/ctxj/NLP-projects-tf/blob/main/NLP_BiLSTM.ipynb) model overfit

## Results
[Saved model](https://github.com/ctxj/NLP-projects-tf/blob/main/NLP_BiLSTM_model.hdf5)  
[Predicted results](https://github.com/ctxj/NLP-projects-tf/blob/main/predict_headlines.csv)

## Acknowledgement
Updated [adam0ling's BERT model](https://github.com/adam0ling/twitter_sentiment/blob/main/3_BERT.ipynb) to work with the lastest version

## License
![Apache License 2.0](https://img.shields.io/badge/License-Apache--License--2.0-green.svg)