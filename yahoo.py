from yahoo_finance import Share

sp = Share('^GSPC')
sp_price, sp_percent_change, sp.change = sp.get_price(), sp.get_percent_change(), sp.get_change()

nasdaq = Share('^IXIC')
nasdaq_price, nasdaq_percent_change, nasdaq_change = nasdaq.get_price(), nasdaq.get_percent_change(), nasdaq.get_change()

# dow = Share('^DJI')
# dow_price, dow_percent_change, dow_change = dow.get_price(), dow.get_percent_change(), dow.get_change()

