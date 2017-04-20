from analyze import Beta

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







