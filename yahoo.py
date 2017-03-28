from yahoo_finance import Share



sp = Share('^GSPC')
sp_price, sp_percent_change, sp.change = sp.get_price(), sp.get_percent_change(), sp.get_change()

nasdaq = Share('^IXIC')
nasdaq_price, nasdaq_percent_change, nasdaq_change = nasdaq.get_price(), nasdaq.get_percent_change(), nasdaq.get_change()

# dow = Share('^DJI')
# dow_price, dow_percent_change, dow_change = dow.get_price(), dow.get_percent_change(), dow.get_change()

def portfolio_stocks(a):
	tickers = []
	index = 0
	for stock in a:
		names = [
		'Company Name', 
		'Ticker', 
		'Price', 
		'P/E Ratio', 
		'Earnings Yield', 
		'Div Yield',
		'50 Day MA',
		'200 Day MA',
		'Price Target'
		]
		ticker = Share(stock)
		comp_name = ticker.get_name()
		tick = stock
		price = ticker.get_price()
		pe = ticker.get_price_earnings_ratio()
		earn_yield = float(ticker.get_EPS_estimate_next_year())/float(ticker.get_price())
		ey = float('%.5f' % earn_yield)*100
		div = ticker.get_dividend_yield()
		final_div = 0 if div == None else div
		fifty = ticker.get_50day_moving_avg()
		two_hundred = ticker.get_200day_moving_avg()
		target = ticker.get_one_yr_target_price()
		values = [comp_name, tick, price, pe, ey, final_div, fifty, two_hundred, target]
		final_values = list(zip(names, values))
		index += 1
		tickers.append(final_values)
	return tickers











