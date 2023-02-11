# stock-scraping-API

A stock scraping service that scrapes data from yahoo finance and serves it on a REST API endpoint using fastAPI.

## Installation

Use the package manager [pip] (https://pip.pypa.io/en/stable/) to install the dependencies stored in requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

To start the server, navigate to the directory where project is stored in the terminal and run the following command.

```bash
uvicorn main:app --reload
```

***

To get data related to a single stock, use the endpoint 

```
https://localhost:8000/api/v1/stock/{symbol}
```

where {symbol} is the ticker of the stock for which data is required.

**Example:** You want to get data for Microsoft:
Use the endpoint 

```
https://localhost:8000/api/v1/stock/MSFT
```

***

To get data related to multiple stocks, use the endpoint 

```
https://localhost:8000/api/v1/stocks/?{query} 
```

where {query} is the list of tickers of the stocks for which data is required.

**Example:** You want to get data for Microsoft and Apple:
Use the endpoint 

```
https://localhost:8000/api/v1/stocks/?q=MSFT&q=AAPL
```

***

Please note that since it **scrapes** and then serves the data, it takes a while to do so because of network constraints in download the page to be scraped.

***

## Features

- [x] Single stock data
- [x] Multiple stock data
- [x] Multiprocessing
- [ ] Filtering functionality

## Contributing

Pull requests are welcome. Feel free to contribute!


