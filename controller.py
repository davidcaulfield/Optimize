from flask import Flask, render_template, session
import models


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/build-portfolio")
def build_portfolio():
	return render_template("build-portfolio.html")


	











if __name__=="__main__":
	app.run(host="127.0.0.1", port=5000, debug=True)



