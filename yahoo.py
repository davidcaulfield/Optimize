from yahoo_finance import Share
from config import _token
import requests
import json

sp = Share('^GSPC')
sp_price, sp_percent_change, sp.change = sp.get_price(), sp.get_percent_change(), sp.get_change()

nasdaq = Share('^IXIC')
nasdaq_price, nasdaq_percent_change, nasdaq_change = nasdaq.get_price(), nasdaq.get_percent_change(), nasdaq.get_change()


def get_dow():
	base = "http://globalindiceshistorical.xignite.com/xglobalindiceshistorical.json/GetLastClosingIndexValue"
	params = dict(
		IdentifierType="Symbol",
		Identifier="DJI2MN.IND_DJI",
		_fields=["Value.Close",
		"Value.PercentChangeFromPreviousClose"],
		_token=_token
		)
	response = requests.get(base, params)
	return response.json()

dow = get_dow()
dow_price = dow['Value']['Close']
final_dow = '%.2f' % dow_price
dow_change = dow['Value']['PercentChangeFromPreviousClose']
final_dow_change = '%.2f' % dow_change
float_dow = float(final_dow_change)


def portfolio_stocks(stocks):
	tickers = []
	index = 0
	for stock in stocks:
		names = [
		'Company Name', 
		'Ticker', 
		'Price',
		'Market Cap', 
		'P/E Ratio', 
		'Earnings Yield', 
		'Div Yield',
		'50 Day MA',
		'200 Day MA',
		'Price Target'
		]
		ticker = Share(stock)
		
		comp_name = ticker.get_name() #company name
		
		tick = stock #ticker
		
		price = ticker.get_price() #price

		market_cap = ticker.get_market_cap() #market_cap

		pe = ticker.get_price_earnings_ratio() #gets pe as a string 
		pe_two = float(pe) if pe else 0 #returns a float of the p/e if there is a result, otherwise returns 0
		final_pe = pe_two if float(pe_two) > 0 else 0 #returns pe_two if > 0 else returns 0

		EPS = ticker.get_EPS_estimate_current_year() # gets eps as a string
		final_eps = EPS if EPS else 0 #returns eps if there is a result, else returns 0
		
		earn_yield = float(final_eps)/float(price) #returns float of earnings yield
		pos_ey = earn_yield if earn_yield > 0 else 0 #turns negitive numbers to 0
		ey = float('%.2f' % float(pos_ey))*100 #returns in % format
		
		div = ticker.get_dividend_yield() #returns div in string
		final_div = 0 if div == None else float(div) #if no result returns 0 else returns float of div 
		
		fifty = ticker.get_50day_moving_avg() #returns as string
		short_fifty = '%.2f' % float(fifty) #returns div with 2 decimal places
		two_hundred = ticker.get_200day_moving_avg() #returns as string
		short_two = '%.2f' % float(two_hundred) #returns float with 2 decimal places

		target = ticker.get_one_yr_target_price() #returns as string
		short_target = '%.2f' % float(target)

		values = [comp_name, tick, price, market_cap, final_pe, ey, final_div, short_fifty, short_two, short_target]
		final_values = list(zip(names, values))
		index += 1
		tickers.append(final_values)
	return tickers















