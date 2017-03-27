from yahoo_finance import Share

sp = Share('^GSPC')
sp_price, sp_percent_change, sp.change = sp.get_price(), sp.get_percent_change(), sp.get_change()

nasdaq = Share('^IXIC')
nasdaq_price, nasdaq_percent_change, nasdaq_change = nasdaq.get_price(), nasdaq.get_percent_change(), nasdaq.get_change()

# dow = Share('^DJI')
# dow_price, dow_percent_change, dow_change = dow.get_price(), dow.get_percent_change(), dow.get_change()

def portfolio_stocks(*args):
	stocks = list(args)
	for i in stocks:
		j=0
		b = Share(i)
		price = b.get_price()
		print(price)
		# performance =  
		target = b.get_one_yr_target_price()
		print(target)
		pe = b.get_price_earnings_ratio()
		print(pe)
		help = dict(i=[stocks[j], price, target, pe])
		j+=1
		return help
		# return price, target, pe
