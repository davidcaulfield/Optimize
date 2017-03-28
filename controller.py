from flask import Flask, render_template, session, request
import requests
import models
# from wrapper import Global_Historical
import wrapper
import yahoo
# from analyze import Stock
# import analyze



app = Flask(__name__)

app.config['SECRET_KEY'] = open('secret_key', 'rb').read()

@app.route("/")
def home():
	return render_template("index.html",
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
	print(username, password)
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
	stocks = stock_list
	stock = yahoo.portfolio_stocks(stocks)
	return render_template("analyzed.html", stocks=stock)

@app.route("/stock-info/<nn>", methods=['POST'])
def stock_info(nn):
	compare_info = analyze.Stock(nn)
	return render_template("stock-info.html")
		# name=compare_info.name,
		# pe=compare_info.pe,
		# ey=compare_info.ey,
		# div=compare_info.div,
		# target=compare_info.target
		# )











if __name__=="__main__":
	app.run(host="127.0.0.1", port=5001, debug=True)



