from yahoo_finance import Share

sp = Share('^GSPC')
sp_price, sp_percent_change, sp.change = sp.get_price(), sp.get_percent_change(), sp.get_change()

nasdaq = Share('^IXIC')
nasdaq_price, nasdaq_percent_change, nasdaq_change = nasdaq.get_price(), nasdaq.get_percent_change(), nasdaq.get_change()

# dow = Share('^DJI')
# dow_price, dow_percent_change, dow_change = dow.get_price(), dow.get_percent_change(), dow.get_change()

def portfolio_stocks(*args):
	stocks = list(args)

	dictt = []
	j=0
	for stock in stocks:
		# j=stock
		b = Share(stock)
		price = b.get_price()
		# print(price) 
		target = b.get_one_yr_target_price()
		# print(target)
		pe = b.get_price_earnings_ratio()
		# print(pe)
		help = dict(stock=[stocks[j], price, target, pe])
		j+=1
		dictt.append(help)
	print(dictt,'''












		''')
	return dictt
		# return price, target, pe
