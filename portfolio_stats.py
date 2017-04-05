import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta

from analyze import Beta


# class Portfolio:

# 	def __init__(self, tickers):
# 		self.tickers = tickers
# 		self.end_date = date.today()
# 		self.start_date = self.end_date - timedelta(days=365)
# 		self.sp_returns = self.get_sp_returns()
# 		self.portfolio_data = self.portfolio_data()
# 		self.portfolio_returns = self.portfolio_returns()
# 		self.combine = self.combine()



# 	def get_sp_returns(self):
# 		sp = web.DataReader('^GSPC','yahoo',self.start_date, self.end_date)
# 		data = pd.DataFrame({'sp_adj_close':sp['Adj Close']}, index=sp.index) #creates dataframe with sp prices and dates
# 		data[['sp_returns']] = (data[['sp_adj_close']]-data[['sp_adj_close']].shift(1))/data[['sp_adj_close']].shift(1)*100
# 		sp_returns = data.dropna()
# 		final = sp_returns['sp_returns']
# 		a = final.tolist()
# 		b = np.array(a)
# 		return b

# 	def portfolio_data(self):
# 		a = []
# 		for i in self.tickers:
# 			stock = web.DataReader(i,'yahoo',self.start_date, self.end_date)
# 			data = pd.DataFrame({'stock_adj_close':stock['Adj Close']}, index=stock.index)
# 			data[['stock_returns']] = (data[['stock_adj_close']]-data[['stock_adj_close']].shift(1))/data[['stock_adj_close']].shift(1)*100
# 			stock_return = data.dropna()
# 			change_list = stock_return['stock_returns']
# 			a.append(change_list)
# 		group = zip(*a)
# 		return group

# 	def portfolio_returns(self):
# 		portfolio = self.portfolio_data
# 		final = []
# 		for i in portfolio:
# 			stock = sum(i)/len(i)
# 			final.append(stock)
# 		finals = np.array(final)
# 		return finals

# 	def combine(self):
# 		a = self.portfolio_returns
# 		b = self.sp_returns
# 		c = np.cov(a, b)
# 		return c

def portfolio_beta_list(stocks):
	beta_list = []
	for i in stocks:
		stock = Beta(i)
		beta = float(stock.calculate_beta())
		beta_list.append(beta)
	return beta_list

def calculate_portfolio_beta(stocks):
	beta_list = portfolio_beta_list(stocks)
	beta = sum(beta_list)/len(beta_list)
	final_beta = '%.2f' % beta
	return final_beta

def portfolio_alpha_list(stocks):
	alpha_list = []
	for i in stocks:
		stock = Beta(i)
		alpha = float(stock.calculate_alpha())
		alpha_list.append(alpha)
	return alpha_list

def calculate_portfolio_alpha(stocks):
	alpha_list = portfolio_alpha_list(stocks)
	alpha = sum(alpha_list)/len(alpha_list)
	final_alpha = '%.2f' % alpha
	return final_alpha







