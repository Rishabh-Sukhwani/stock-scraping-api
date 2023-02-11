from Scrape import Scrape
import json

elements_to_scrape = {} 

f = open("scrape.json")
data = f.read()
f.close()
elements_to_scrape = json.loads(data)

def process_data(ticker, elements_to_scrape):
    stock = Scrape(ticker, elements_to_scrape)
    stock_data = stock.summary()
    stock_data_updated = {"symbol": ticker,"data": stock_data}
    return stock_data_updated