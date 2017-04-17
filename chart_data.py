import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta


def get_sp():
	end_date = date.today()
	start_date = end_date - timedelta(days=365)
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returns_list = returns.tolist()
	short_list = []
	for i in returns_list:
		short = '%.2f' % i
		short_list.append(short)
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	sp_name = ['S&P500']
	sp_final = sp_name+short_list
	date_name = ['Dates']
	final_date = date_name+date_list
	return dict(date_list=final_date, adj_list=sp_final)

def get_stock_data(ticker):
	end_date = date.today()
	start_date = end_date - timedelta(days=365)
	stock = web.DataReader(ticker,'yahoo', start_date, end_date)
	adj = stock['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returns = returns.tolist()
	name = [ticker]
	final = name+returns
	return final

def final_chart_data(ticke):
	sp = get_sp()
	stock = get_stock_data(ticke)
	sp['ticker'] = stock  #adding the new key value pair to dictionary
	return sp


def final_portfolio_returns(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = '%.2f' % float(sum(i)/len(i))
		returns.append(avg_return)
	sp = get_sp()
	sp['Portfolio'] = returns
	last = returns[-2]
	sp_last = '%.2f' % float(sp['adj_list'][-2])
	return sp, last, sp_last





