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
	short_list = []
	for i in returns_list:
		short = '%.2f' % i
		short_list.append(short)
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	final_date_list = date_list[::3]
	sp_name = ['S&P500']
	sp_final = sp_name+short_list
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
		final_list.append(returnss)			
	grouped = zip(*final_list)
	return grouped


def final_portfolio_returns_three(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = sum(i)/len(i)
		short = '%.2f' % avg_return
		returns.append(short)
	total_portfolio_return = float(returns[-2])
	sp = get_sp_three()
	total_sp_return = float('%.2f' % float(sp['adj_list'][-2]))
	sp['Portfolio'] = returns
	return sp, total_portfolio_return, total_sp_return



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
	short_list = []
	for i in returns_list:
		short = '%.2f' % i
		short_list.append(short)
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	final_date_list = date_list[::5]
	sp_name = ['S&P500']
	sp_final = sp_name+short_list
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
		short = '%.2f' % avg_return
		returns.append(short)
	total_portfolio_return = float(returns[-2])
	sp = get_sp_five()
	total_sp_return = float('%.2f' % float(sp['adj_list'][-2]))
	sp['Portfolio'] = returns
	return sp, total_portfolio_return, total_sp_return


