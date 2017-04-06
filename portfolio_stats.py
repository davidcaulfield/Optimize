import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
from datetime import date, timedelta

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

def portfolio_alpha_list(stocks):
	alpha_list = []
	for i in stocks:
		stock = Beta(i)
		alpha = float(stock.calculate_alpha())
		alpha_list.append(alpha)
	return alpha_list

def calculate_portfolio_alpha(stocks):
	alpha_list = portfolio_alpha_list(stocks)
	alpha = sum(alpha_list)/len(alpha_list)
	final_alpha = '%.2f' % alpha
	return final_alpha







