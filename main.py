from itertools import repeat
from fastapi import FastAPI, HTTPException, Query
from requests import HTTPError, TooManyRedirects
from Scrape import Scrape
from data import elements_to_scrape, process_data
import multiprocessing

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/stock/{ticker}")
def summary(ticker: str):
    ticker = ticker.upper()
    try:
        s = Scrape(ticker, elements_to_scrape)
        s_data = s.summary()
    except TooManyRedirects:
        raise HTTPException(status_code=404, detail="{ticker} doesn't exist or cannot be found.")
    except HTTPError:
        raise HTTPException(status_code=500, detail="An error has occurred while processing the request.")

    return s_data

@app.get("/api/v1/stocks/")
async def read_items(q: list[str] | None = Query(default=None)):
    Q = map(lambda x: x.upper(), q)
    Q = list(Q)
    print(Q)
    try:
        with multiprocessing.Pool() as pool:
            results = pool.starmap(process_data, zip(Q, repeat(elements_to_scrape)))
            #print(results)
            final_dict = {d["symbol"]: d["data"] for d in results}
            #print(final_dict)
    except HTTPError as e:
        print(f"Encountered an error while scraping data: {e}")
    
    return final_dict
        