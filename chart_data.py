import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta





def get_sp():
	end_date = date.today()
	start_date = end_date - timedelta(days=252)
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returns_list = returns.tolist()
	print(returns_list)
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	sp_name = ['S&P500']
	sp_final = sp_name+returns_list
	date_name = ['Dates']
	final_date = date_name+date_list
	return dict(date_list=final_date, adj_list=sp_final)


def get_stock_data(ticker):
	end_date = date.today()
	start_date = end_date - timedelta(days=252)
	stock = web.DataReader(ticker,'yahoo', start_date, end_date)
	adj = stock['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returns = returns.tolist()
	name = [ticker]
	final = name+returns
	return final

def final_chart_data(ticker):
	sp = get_sp()
	stock = get_stock_data(ticker)
	sp['ticker'] = stock
	return sp

print(get_sp())
