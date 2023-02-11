import requests
from bs4 import BeautifulSoup

class Scrape():

    def __init__(self, symbol, elements):
        url = "https://finance.yahoo.com/quote/" + symbol

        r = requests.get(url)
        if(r.url != url):
            raise requests.TooManyRedirects()

        r.raise_for_status()
        
        self.soup = BeautifulSoup(r.text, "html.parser")

        self.__summary = {}

        for el in elements["elements"]:
            tag = self.soup.select_one(el["from"])

            if tag != None:
                self.__summary[el["to"]] = tag.get_text()

    def summary(self):
        return self.__summary