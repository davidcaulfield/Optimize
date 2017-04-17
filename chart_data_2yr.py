import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta
from chart_data import get_sp


# 3 = 1095
# 5 = 1825

# =====================3 Year Returns=====================================================


def portfolio_returns(tickers, day, step):
	final_list = []
	for i in tickers:
		end_date = date.today()
		start_date = end_date - timedelta(days=day)
		stock = web.DataReader(i,'yahoo', start_date, end_date)
		adj = stock['Adj Close']
		first_price = adj.iloc[0]
		percent_returns = lambda x: (x/first_price-1)*100
		returns = adj.apply(percent_returns)
		print(step, day)
		returnss = returns[::step]
		final_list.append(returnss)			
	grouped = zip(*final_list)
	return grouped


def final_portfolio_returns_three(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = '%.2f' % float(sum(i)/len(i))
		returns.append(avg_return)
	print('len', len(returns))
	total_portfolio_return = float(returns[-2])
	sp = get_sp(1095, 3)
	total_sp_return = float('%.2f' % float(sp['adj_list'][-2]))
	sp['Portfolio'] = returns
	return sp, total_portfolio_return, total_sp_return



# =====================5 Year Returns=====================================================

def portfolio_returns_five(tickers, day, step):
	final_list = []
	for i in tickers:
		end_date = date.today()
		start_date = end_date - timedelta(days=day)
		stock = web.DataReader(i,'yahoo', start_date, end_date)
		adj = stock['Adj Close']
		first_price = adj.iloc[0]
		percent_returns = lambda x: (x/first_price-1)*100
		returns = adj.apply(percent_returns)
		returnss = returns[::step]
		final_list.append(returnss)			
	grouped = zip(*final_list)
	return grouped


def final_portfolio_returns_five(portfolio):
	returns = ['Portfolio']
	for i in portfolio:
		avg_return = sum(i)/len(i)
		short = '%.2f' % avg_return
		returns.append(short)
	print('len', len(returns))
	total_portfolio_return = float(returns[-2])
	sp = get_sp(1825, 5)
	total_sp_return = float('%.2f' % float(sp['adj_list'][-2]))
	sp['Portfolio'] = returns
	return sp, total_portfolio_return, total_sp_return


