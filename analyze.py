import yahoo


fundamentals = yahoo.portfolio_stocks()

def compare_beta():
	if stock_beta < 1:
		result = "This stock is risky than the market."
	elif stock_beta < 0:
		result = '''This stock tends to move in the opposite direction.
This property gives the investor protection when the market falls.'''
	elif stock_beta >= 1 and stock_beta <= 1.5:
		result = '''This stock tends to move in the same direction as the market, 
but its movements are slightly more dramatic. When the market 
is rising, this stock tends to produce slightly superior returns 
compared to the market. When the market falls, this stock tends to 
fall by a greater percentage than the overall market.'''
	elif stock_beta > 1.5:
		result = '''This stock has been significantly more volitale than the market
in the past and this makes it a risky stock to hold. This company tends
to be 50\%' more volitale than the market. This means that when the 
market is rising, you can expect to to earn significantly higher 
returns than the market, but when the market is falling, you should
expect to lose significantly more than the market.'''
	return result


def compare_pe():
	if stock_pe in range((index_pe - 1.5), (index_pe + 1.5)):
		result = '''This stock has a price-to-earnings ratio that is very
close to the market price-to-earnings ratio. This means that the stock and
S&P500 are valued at about the same level.'''
	elif stock_pe < (index_pe - 1.5):
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
	elif stock_pe > (index_pe + 1.5):
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














