from flask import Flask, render_template, request 				#request is used to handle the input from user (form data)
from forecast import weather_func, forecast_func
import requests

app = Flask(__name__)
@app.route('/') 									#define route for the homepage	
def location(): 									#function that will render location.html which have form that will take user input
	return render_template('location.html')

@app.route('/weather', methods=['POST'])			# this weather route will accept POST request from the location html form (user input)
def weather():										#function for current weather and forecast
	city = request.form['city']						#this will retrieve the city name from the form (user input)
	data1 = weather_func(city)						#this call the weather function to get current weather
	data2 = forecast_func(city)						#this call the forecast function to get the forecast
	return render_template('weather.html', weather_data=data1, forecast_data=data2)			#this will return the data retrieve from the function to the weather html

if __name__=='__main__':
	app.run(debug=True)