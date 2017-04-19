import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta


def get_sp(day, step):
	end_date = date.today()
	start_date = end_date - timedelta(days=day)
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returnss =returns[::step]
	returns_list = returnss.tolist()
	short_list = []
	for i in returns_list:
		short = '%.2f' % i
		short_list.append(short)
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	final_date_list = date_list[::step]
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

def final_chart_data(ticker):
	sp = get_sp(365, 1)
	stock = get_stock_data(ticker)
	sp['ticker'] = stock  #adding the new key value pair to dictionary
	return sp # returns the data for individual stocks vs sp chart


def final_portfolio_returns(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = '%.2f' % float(sum(i)/len(i))
		returns.append(avg_return) #gets average daily return for portfolio 
	last = returns[-2] #gets total return for portfolio over timeframe
	sp = get_sp(365, 1)
	sp['Portfolio'] = returns
	sp_last = '%.2f' % float(sp['adj_list'][-2])
	return sp, last, sp_last





