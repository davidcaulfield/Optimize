from flask import Flask, render_template, session, request
import requests
import models
# from wrapper import Global_Historical
import wrapper
import yahoo
from analyze import Stock, Beta
# import analyze
from yahoo_finance import Share
from chart_data import *
import json


app = Flask(__name__)

app.config['SECRET_KEY'] = open('secret_key', 'rb').read()

@app.route("/")
def home():
	return render_template("index.html",
		dow_price=yahoo.dow_price,
		dow_percent_change=yahoo.dow_change,
		sp_price=yahoo.sp_price,
		sp_percent_change=yahoo.sp_percent_change,
		nasdaq_price=yahoo.nasdaq_price,
		nasdaq_percent_change=yahoo.nasdaq_percent_change)


@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/check-login", methods=["POST"])
def check_login():
	username = request.form['user']
	password = request.form['password']
	result = models.User.login(username, password)
	if result:
		session['username'] = username
		return dashboard()
	else:
		return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/check-register", methods=["POST"])
def check_register(): 
	username = request.form['user']
	result = models.User.check_register(username)
	if result:
		return render_template("register.html")
	else:
		models.User.register(**request.form)
		session['username'] = username
		return dashboard()

@app.route("/build-portfolio")
def build_portfolio():
	return render_template("build-portfolio.html")

@app.route("/dashboard")
def dashboard():
	username = session['username']
	user_id = models.User.get_user_id(username)
	return render_template("dashboard.html", user=username)

@app.route("/analyze", methods=['POST'])
def analyze():
	objective = request.form['objective']
	time = request.form['time']
	stocks_input = request.form['stocks']
	stocks = stocks_input.split(",")
	return analyzed(objective, time, stocks)

@app.route("/analyzed")
def analyzed(objective, time, stock_list):
	stock = yahoo.portfolio_stocks(stock_list)
	portfolio = portfolio_returns(stock_list)
	final = final_portfolio_returns(portfolio)
	json_portfolio = json.dumps(final)
	return render_template("analyzed.html", stocks=stock, portfolio=json_portfolio)

@app.route("/stock-info/<ticker>", methods=['POST'])
def stock_info(ticker):
	stock = Share(ticker)
	name = stock.get_name()
	price = stock.get_price()
	pe = stock.get_price_earnings_ratio()
	EPS = float(stock.get_EPS_estimate_current_year())
	earn_yield = float(price)/EPS
	final_yield = '%.2f' % earn_yield
	print(final_yield)
	div = stock.get_dividend_yield()
	final_div = 0 if div == None else div
	target = stock.get_one_yr_target_price()
	fifty = stock.get_50day_moving_avg()
	two_hundred = stock.get_200day_moving_avg()
	info = Stock(name, price, pe, final_yield, final_div, target, fifty, two_hundred)
	beta = Beta(ticker)
	return render_template("stock-info.html",
		name=info.name,
		num_beta=beta.calculate_beta(),
		beta=beta.compare_beta(),
		pe_num = pe,
		pe=info.compare_pe(),
		ey_num=final_yield,
		ey=info.compare_earn_yield(),
		div_num=final_div,
		div=info.compare_div(),
		target_num=target,
		target=info.compare_target())

@app.route("/chart-data/<ticker>", methods=['GET', 'POST'])
def chart_data(ticker):
	data = final_chart_data(ticker)
	return json.dumps(data)





if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)



