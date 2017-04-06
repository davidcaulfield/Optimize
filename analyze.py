import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date

class Beta:

	def __init__(self, symbol):

		self.symbol = symbol
		self.start_date = date(2012,3,20)
		self.end_date = date(2017,4,3)
		self.period = 12
		self.stock_returns = self.calculate_stock_returns()
		self.sp_returns = self.calculate_sp_returns()
		# self.alpha = self.calculate_alpha()

	def get_data(self):
		stock = web.DataReader(self.symbol,'yahoo',self.start_date, self.end_date)
		return stock

	def get_sp_data(self):
		sp = web.DataReader('^GSPC','yahoo',self.start_date, self.end_date)
		return sp


	def calculate_stock_returns(self):
		stock = self.get_data()
		data = pd.DataFrame({'stock_adj_close':stock['Adj Close']}, index=stock.index)
		data[['stock_returns']] = data[['stock_adj_close']]/data[['stock_adj_close']].shift(1)
		stock_return = data.dropna()
		return stock_return
	
	def calculate_sp_returns(self):
		sp = self.get_sp_data()
		data = pd.DataFrame({'sp_adj_close':sp['Adj Close']}, index=sp.index)
		data[['sp_returns']] = data[['sp_adj_close']]/data[['sp_adj_close']].shift(1)
		sp_return = data.dropna()
		return sp_return

	def variance(self):
		sp = self.calculate_sp_returns()
		returns = sp['sp_returns']
		var = np.var(returns)
		return var

	def compute_covariance(self):
		covariance = np.cov(self.stock_returns['stock_returns'], self.sp_returns['sp_returns'])
		return covariance

	def calculate_beta(self):
		covariance = self.compute_covariance()
		var = self.variance()
		beta = '%.2f' % (covariance[0,1]/var)

		return beta

	def compare_beta(self):
		stock_beta = self.calculate_beta()
		if float(stock_beta) < 1:
			result = "This stock is risky than the market."
		elif float(stock_beta) < 0:
			result = '''This stock tends to move in the opposite direction.
	This property gives the investor protection when the market falls.'''
		elif float(stock_beta) >= 1 and float(stock_beta) <= 1.3:
			result = '''This stock tends to move in the same direction as the market, 
	but its movements are slightly more dramatic. When the market 
	is rising, this stock tends to produce slightly superior returns 
	compared to the market. When the market falls, this stock tends to 
	fall by a greater percentage than the overall market.'''
		elif float(stock_beta) > 1.3:
			result = '''This stock has been significantly more volitale than the market
	in the past and this makes it a risky stock to hold. This company tends
	to be 50\%' more volitale than the market. This means that when the 
	market is rising, you can expect to to earn significantly higher 
	returns than the market, but when the market is falling, you should
	expect to lose significantly more than the market.'''
		return result






	# def calculate_alpha(self):
	# 	beta = self.calculate_beta()
	# 	alpha = np.mean(self.stock_returns['stock_returns'])
	# 	i = float(beta)*np.mean(self.sp_returns['sp_returns'])
	# 	j = alpha - i
	# 	annualized_alpha = j*self.period
	# 	return annualized_alpha

	# def calculate_r_squared(self):
	# 	covariance = self.compute_covariance()
	# 	alpha = self.calculate_alpha()
	# 	beta = self.calculate_beta()
	# 	ypred = alpha+beta*self.sp_returns['sp_returns']
	# 	ss_res = np.sum(np.power(ypred-self.stock_returns['stock_returns'],2))
	# 	ss_tot = covariance[0,0]*(len(self.stock_returns)-1)
	# 	r_squared = 1.-ss_res/ss_tot
	# 	return r_squared




class Stock:

	def __init__(self, name, price, market_cap, pe, earn_yield, final_div, target, fifty, two_hundred):
		self.name = name
		# self.beta = self.compare_beta()
		self.price = price
		self.market_cap = market_cap
		self.pe = pe
		self.ey = earn_yield
		self.div = final_div
		self.target = target
		self.stock_fifty = fifty
		stock_two_hundred = two_hundred


	def compare_beta(self):
		if stock_beta < 1:
			result = "This stock is risky than the market."
		elif stock_beta < 0:
			result = '''This stock tends to move in the opposite direction.
	This property gives the investor protection when the market falls.'''
		elif stock_beta >= 1 and stock_beta <= 1.3:
			result = '''This stock tends to move in the same direction as the market, 
	but its movements are slightly more dramatic. When the market 
	is rising, this stock tends to produce slightly superior returns 
	compared to the market. When the market falls, this stock tends to 
	fall by a greater percentage than the overall market.'''
		elif stock_beta > 1.3:
			result = '''This stock has been significantly more volitale than the market
	in the past and this makes it a risky stock to hold. This company tends
	to be 50\%' more volitale than the market. This means that when the 
	market is rising, you can expect to to earn significantly higher 
	returns than the market, but when the market is falling, you should
	expect to lose significantly more than the market.'''
		return result

	def market_cap_explain(self):
		pass

	def compare_pe(self):
		if float(self.pe) > (17.5 - 1.5) and float(self.pe) < (17.5 + 1.5):
			result = '''This stock has a price-to-earnings ratio that is very
	close to the market price-to-earnings ratio. This means that the stock and
	S&P500 are valued at about the same level.'''
		elif float(self.pe) < (17.5 - 1.5):
			result =  '''This stock has a lower price-to-earnings ratio than the
	market. This means that investors are giving this stock a lower valuation
	than they are giving to the market. This happens for a few different reasons.
	First, this stock could be undervalued compared to the market. Investors could
	be overlooking the company and this creates a value opportunity for investors.
	Second, the company could have a lower p/e ratio because it is a lower quality
	company than the average company in the S&P500. This company can have lower
	quality growth, earnings, etc which justifies its lower p/e ratio. Third, the
	company could be in an industry where it is normal for p/e ratios to be different
	from the market.'''
		elif float(self.pe) > (1.95 + 1.5):
			result = '''This stock has a higher price-to-earnings ratio than the
	market. This means that investors are giving this stock a higher valuation
	than they are giving to the market. This happens for a few different reasons.
	First, investors could be placing a higher value on this company compared to
	the market for no good reason. This would mean that the stock is overvalued
	and investors should be careful.Second, the company could have a higher p/e
	ratio because it has higher quality growth, earnings, etc which justifies its
	higher p/e ratio. Third, the company could be in an industry where it is normal
	for p/e ratios to be different from the market.'''
		return result


	def compare_earn_yield(self):
		if float(self.ey) > 3:
			result = '''This company has a higher earnings yield than the market.
	This is a good sign and means that the company is of good quality.'''
		elif float(self.ey) < 3:
			result = '''This company has a lower earnings yield than the market.
	This is a bad sign and investors should ask questions as to why this, 
	is happening.'''
		return result


	def compare_div(self):
		if float(self.div) > 1.95:
			result = '''This company has a higher dividend yield than the
	market. This is a good sign for investors who are looking to generate
	income from their investments. However, a high dividend yield
	could mean that the company isn't reinvesting into growth and
	and it is unlikely to see high earnings growth or capital apprciation.'''
		elif float(self.div) < 1.95:
			result = '''This company has a lower dividend yield than the
	market. This is a bad sign for investors who are looking to generate
	income from their investments. However, a low dividend yield
	could mean that the company is reinvesting into growth and
	and that could lead to earnings growth and stock appreciation.'''
		return result

	def compare_ma(self):
		if float(self.stock_fifty) > float(self.stock_two_hundred):
			result = '''This stocks 50 day moving average is above its 200
	day moving average. This is a bullish sign. It means that there is
	short term momentum in the stock. Investors should watch for the moment
	when the 50 day moving average drops below the 200 day moving average.
	This is a bearish sign and means the the short term average price of the
	stock is trading below its long term average price and is losing 
	momentum.'''
		elif float(self.stock_fifty) < float(self.stock_two_hundred):
			result = '''This stocks 50 day moving average is below its 200
	day moving average. This is a bearish sign. It means that there is
	no short term momentum in the stock. Investors should watch for the moment
	when the 50 day moving average crosses above the 200 day moving average.
	This is a bullish sign and means the the short term average price of the
	stock is above its long term average price and is gaining momentum.''' 
		return result

	def compare_target(self):
		if float(self.target) > float(self.price):
			result = '''The target price for this stock is above its
	current price. This is a good sign because it means analysts 
	believe the stock is going to appreciate in value.'''
		elif float(self.target) < float(self.price):
			result = '''The target price for this stock is below its
	current price. This is a bad sign because it means analysts 
	believe the stock is going to depreciate in value.'''
		return result






