import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta





def get_sp():
	end_date = date.today()
	start_date = end_date - timedelta(days=252)
	sp = web.DataReader('^GSPC','yahoo', start_date, end_date)
	adj = sp['Adj Close']
	adj_list = adj.tolist()
	datee = sp.index.values
	date_list = []
	for day in datee:
		correct = str(day)[:10]
		date_list.append(correct)
	return dict(date_list=date_list, adj_list=adj_list)


def get_stock_data(ticker):
	end_date = date.today()
	start_date = end_date - timedelta(days=252)
	stock = web.DataReader(ticker,'yahoo', start_date, end_date)
	adj = stock['Adj Close']
	adj_list = adj.tolist()
	return adj_list

def final_chart_data(ticker):
	sp = get_sp()
	stock = get_stock_data(ticker)
	sp['ticker'] = stock
	return sp
