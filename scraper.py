#Scraper for a dynamic site, seekingalpha.com
#Scrape stock's news headlines and their dates

#Imports
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Download and direct chrome driver
PATH = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe" #Path to chromedriver
driver = webdriver.Chrome(PATH)

#Ticker for stock news to scrape
ticker = "FB"
date_xpath = "__7a760-bAtK_ __7a760-uJXfc" #Check xpath from url, as they change when there's sit update
headline_xpath = "__7a760-3a6i8"

#Function for scraping dynamic site
def load_page(ticker, date_xpath, headline_xpath):
    
    df = pd.DataFrame(columns=['Date', 'Headlines'])
    dates = []
    headlines = []

    url = f"https://seekingalpha.com/symbol/{ticker}/news?filter="


    driver.get(url)
    print(url)

    time.sleep(2)

    #Loop for loading dynamic site to the end of page
    for i in range(600):
        body = driver.find_element_by_xpath('//body')
        body.send_keys(Keys.END)
        time.sleep(.5)

    #Find xpaths and append them to dataframe
    date = driver.find_elements_by_xpath(f'//span[@class="{date_xpath}"]')
    headline = driver.find_elements_by_xpath(f'//a[@class="{headline_xpath}"]')

    elements_in_page = len(headline)
    for element in range(elements_in_page):
        headlines.append(headline[element].text)
        dates.append(date[element].text)

    df["Date"] = dates
    df["Headlines"] = headlines

    df.drop_duplicates()
    print(len(df))
    
    df.to_csv(f"{ticker}_headlines.csv", index=False)

#Execute and function
load_page(ticker=ticker, headline_xpath=headline_xpath, date_xpath=date_xpath)