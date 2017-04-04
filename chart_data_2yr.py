import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta




# =====================3 Year Returns=====================================================
def get_sp_three():
	end_date = date.today()
	start_date = end_date - timedelta(days=1095)
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returnss =returns[::3]
	returns_list = returnss.tolist()
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	final_date_list = date_list[::3]
	sp_name = ['S&P500']
	sp_final = sp_name+returns_list
	date_name = ['Dates']
	final_date = date_name+final_date_list
	return dict(date_list=final_date, adj_list=sp_final)



def portfolio_returns_three(tickers):
	final_list = []
	for i in tickers:
		end_date = date.today()
		start_date = end_date - timedelta(days=1095)
		stock = web.DataReader(i,'yahoo', start_date, end_date)
		adj = stock['Adj Close']
		first_price = adj.iloc[0]
		percent_returns = lambda x: (x/first_price-1)*100
		# stock["Percent Change"] = (stock['Adj Close'].shift(3)/first_price-1) * 100
		returns = adj.apply(percent_returns)
		# returns = stock["Percent Change"].fillna(0)
		# returns.fillna(0)
		returnss = returns[::3]
		# print(returnss)
		final_list.append(returnss)			
	grouped = zip(*final_list)
	return grouped

portfolio_returns_three(["AAPL", "MO"])

def final_portfolio_returns_three(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = sum(i)/len(i)
		returns.append(avg_return)
	sp = get_sp_three()
	sp['Portfolio'] = returns
	return sp



# =====================5 Year Returns=====================================================

def get_sp_five():
	end_date = date.today()
	start_date = end_date - timedelta(days=1825)
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	first_price = adj.iloc[0]
	percent_returns = lambda x: (x/first_price-1)*100
	returns = adj.apply(percent_returns)
	returnss = returns[::5]
	returns_list = returnss.tolist()
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	final_date_list = date_list[::5]
	sp_name = ['S&P500']
	sp_final = sp_name+returns_list
	date_name = ['Dates']
	final_date = date_name+final_date_list
	return dict(date_list=final_date, adj_list=sp_final)

def portfolio_returns_five(tickers):
	final_list = []
	for i in tickers:
		end_date = date.today()
		start_date = end_date - timedelta(days=1825)
		stock = web.DataReader(i,'yahoo', start_date, end_date)
		adj = stock['Adj Close']
		first_price = adj.iloc[0]
		percent_returns = lambda x: (x/first_price-1)*100
		# stock["Pecent Change"] = (stock['Adj Close']/first_price-1) * 100
		returns = adj.apply(percent_returns)
		returnss = returns[::5]
		returns = returnss.tolist()
		final_list.append(returns)			
	grouped = zip(*final_list)
	return grouped


def final_portfolio_returns_five(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = sum(i)/len(i)
		returns.append(avg_return)
	sp = get_sp_five()
	sp['Portfolio'] = returns
	return sp


