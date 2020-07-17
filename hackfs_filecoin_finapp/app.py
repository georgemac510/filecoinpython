
from flask import Flask, request, render_template
import yfinance as yf

# find Flask app.
app = Flask(__name__)

# API Route for pulling the stock quote
@app.route("/quote")
def display_quote():

	# default to MSFT
	symbol = request.args.get('symbol', default="MSFT")

	# pull the stock quote
	quote = yf.Ticker(symbol)

	#return the object via the HTTP Response
	return quote.info

# API hookup to access fin data
@app.route("/history")
def display_history():
	#get the query string parameters
	symbol = request.args.get('symbol', default="MSFT")
	period = request.args.get('period', default="2y")
	interval = request.args.get('interval', default="1wk")

	quote = yf.Ticker(symbol)
	# retrieve ticker symbol data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
    # convert data to JSON
	data = hist.to_json()

	return data

# Route to main page
@app.route("/")
def home():
	# Flask renders website template
    return render_template("home.html")

# start the flask app.
if __name__ == "__main__":
	app.run(debug=True)
