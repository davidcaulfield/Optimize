from analyze import Beta
from yahoo import Share



def check_objective(objective, stocks, time):
	if objective == 'Speculation':
		stock = Portfolio_info_speculation(stocks,time)
		return stock.beta_response(stocks), stock.other(time)
	elif objective == 'Income':
		stock = Portfolio_info_income(stocks, time)
		return stock.beta, stock.div


class Portfolio_info_speculation:

	def __init__(self, stocks, time):
		self.betas = self.check_betas(stocks)

#========================Speculation Beta===================================================================== 
	def portfolio_beta_list(self, stocks):
		beta_list = []
		for i in stocks:
			stock = Beta(i)
			beta = float(stock.calculate_beta())
			beta_list.append(beta)
		print(beta_list)
		return beta_list

	def check_betas(self, stocks):
		beta_list = self.portfolio_beta_list(stocks)
		score = 0
		for i in beta_list:
			if i >= 1.3:
				score+=1
			else:
				score+=0
		return score

	def beta_response(self, stocks):
		score = self.check_betas(stocks)
		if score/len(stocks) <= .7:
			return '''Less than 70% of the stocks in your portfolio have a beta that is significantly greater than
the market beta of 1. This means that your portfolio is significantly less volitale than the market.
While this is may be good for investors who want to aviod risk, it does not fit the purpose of this
portfolio. A speculative portfolio should hold a high number of stocks that have betas that are greater
than the market beta. You should look replace some of the low beta stocks in your portfolio with stocks
that have high betas. Look into the technology, biotechnology, mining, and energy stocksc to help
fill these needs.'''
		else:
			return '''Over 70% of the stocks in your portfolio have a beta that is higher than the market beta.
This means that your portfolio is going to be significantly more risky than the market, but this is what you want
when your objective is speculation. A speculative portfilio has a significant risk of loss, but also has a potential
for a significant gain. It is important to make the distinction between speculation and investing. Speculation is
when you make a short term bet that the price of a stock will increse based on factors other than the fundamentals
of the company. Speculation usually occurs in a timeframe of less than a year.'''

#===============================================================================================================
	def other(self, time):
		if time == '1-5 years':
			return '''It is difficut to judge speculative stocks based on fundamentals such as the P/E Ratio or earnings yield.
Investors typically hold these stocks based on a "hunch" that the price will increase. There is no way to judge whether
or not a stock is a "good" speculative speculative stock or not. The choice of these stocks relies on each individual
investors justification for holding the stock.'''
		else:
			return '''It does not make sense to hold a long term specualtive portfolio. Speculation is usually based on 
short term price movements in stocks. If you want to hold stocks over a longer period of time you will need to choose a
new portfolio objective.'''
#===============================================================================================================




class Portfolio_info_income:

	def __init__(self, stock, time):
		self.div = self.div_yield(stock)
		self.beta = self.check_beta(stock)

#==============================Income Dividends===========================================================================
	def div_yield(self, stock):
		div_list = self.get_divs(stock)
		score = self.compare_divs(div_list)
		if score == len(stock)*2:
			return '''Every stock in this portfolio has the type of dividend yield that you want in an income portfolio. Every stock in this
portfolio has a higher dividend yield than the yield on a 10-year risk free bond. Dividend yield is arguarbly the most important thing to consider when 
builing an income portfolio. You want to do some extra research though to make sure that the underlying fundamentals of these
companies are strong. It is important to know that a company with a high dividend yield has enough earning power to continue 
paying its dividend.'''
		elif score >= len(stock) and score <= len(stock)*2:
			return '''This portfolio holds some good stocks to get income, but there is still some room for improvement. The
average yield on a stock in your portfolio is greater than the yield on the S&P500, but less than the yield on a 10-year risk
free bond. You should consider identifying the compainies with dividend yields that are less than the 10-year bond yield in
this portfolio, and replace them with companies that have higher yields. To find these stocks, look in high dividend paying
industries such as utilities, REIT's, and even financial institutions.'''
		else:
			return '''These stocks are not fit for an income portfolio. The aveage dividend yield on a stock in this portfolio is
less than the yield on the S&P500. Consider looking into high dividend paying sectors such as utilities, REIT's, and financial
institutions to find stocks that will provide you with significantly higher yields.'''   

	def get_divs(self, stocks):
		div_list = []
		for i in stocks:
			stock = Share(i)
			div = stock.get_dividend_yield()
			final = div if div else 0
			final_div = float(final)
			div_list.append(final_div)
		return div_list

	def compare_divs(self, div_list):
		score = 0
		for i in div_list:
			if i > 2.64:
				score+=2
			elif i >= 1.94 and i <= 2.64:
				score+=1
			else:
				score+=0
		return score
#=====================================================================================================================

#==================================Income Beta===========================================================================
	def check_beta(self, stocks):
		beta_list = self.portfolio_beta_list(stocks)
		print(beta_list, 'g')
		score = self.score_betas(beta_list)
		print(len(beta_list))
		if score/len(beta_list) < .75:
			return '''More than 25% of the stocks in this portfolio a have a beta that is significantly
higher than the market beta of 1. This is not a good sign in a portfolio designed around an income objective.
Investors who are looking for income want to hold stocks that are less risky than the overall market. This means
finding companies with high dividend yields and betas that are very close to or lower than 1. Look to sectors such
as utilities, REIT's, and financial institutions to find companies that meet these requirements.'''
		else:
			return '''A majority of the stocks in this portfolio have a beta that is less than the market beta. This
means that the portfolio is less voliatile than the market and that is a good thing for income investors. Income
investors try to identify stocks that pay high dividend yields and are less risky than the market. They may not
realize all the potential gains during periods when the market rises significantly, but the can sleep soundly at night
knowing that when the market falls, their low voliatility stocks will lose less than the market and they will still
recieve the dividends.''' 

	def portfolio_beta_list(self, stocks):
		beta_list = []
		for i in stocks:
			stock = Beta(i)
			beta = float(stock.calculate_beta())
			beta_list.append(beta)
		print('geting to bet_list', beta_list, type(beta_list))
		return beta_list

	def score_betas(self, beta_list):
		score = 0
		for i in beta_list:
			if i < 1.1:
				score+=1
			else:
				score+=0
		return score
#===============================================================================================================




