from analyze import Beta




def check_objective(objective, stocks, time):
	if objective == 'Speculation':
		stock = Portfolio_info_speculation(stocks,time)
		return stock.beta_response(stocks), stock.other(time)


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


