from flask import Flask, render_template, session, request
import models


app = Flask(__name__)

app.config['SECRET_KEY'] = open('secret_key', 'rb').read()

@app.route("/")
def home():
	return render_template("index.html")

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
		print('good')
		session['username'] = username
		return dashboard()
	else:
		print('bad')
		return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/check-register", methods=["POST"])
def check_register():
	fname = request.form['fname']
	lname = request.form['lname']
	email = request.form['email']
	phone = request.form['phone'] 
	username = request.form['user']
	password = request.form['pass']
	result = models.User.check_register(username)
	if result:
		return render_template("register.html")
	else:
		models.User.register(fname, lname, email, phone, username, password)
		session['username'] = username
		return dashboard()

@app.route("/build-portfolio")
def build_portfolio():
	return render_template("build-portfolio.html")


	











if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)



