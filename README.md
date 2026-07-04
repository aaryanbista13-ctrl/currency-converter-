# Currency Converter

A Python command line currency converter that fetches live exchange rates 
and saves your conversion history permanently.

## Features
- Convert between any world currencies using live exchange rates
- Saves every conversion to CSV for permanent history
- View full conversion history anytime
- Handles invalid currencies and connection errors

## How to run
pip install requests pandas
python currency_converter.py

## How it works
The program fetches live exchange rates from ExchangeRate-API.
It converts through USD as a base currency in two steps:
1. Convert FROM currency to USD
2. Convert USD to TO currency

## Example
1000 NPR → USD → EUR gives the correct live conversion rate

## What I learned
- Fetching live data from REST APIs
- Two step currency conversion logic
- Saving API results to CSV with Pandas
- Building persistent history with DataFrames

## Libraries used
- requests — for API calls
- pandas — for data storage and history
- os — for file checking
