import requests
def weather_func(city):
	api_key = ''
	weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
	response = requests.get(weather_url)
	weather_data = response.json()
	return weather_data

def forecast_func(city):
	api_key = ''
	forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
	response = requests.get(forecast_url)
	data = response.json()
	forecast_data = []
	count = 0
	for forecast in data['list'][3:]:		#this to extract only relevant data and pass it to single variable
		if count < 7:						#since the forecast data is for 5 days with 3 hour intervals, we limit it to only 7 intervals
			info = {
				'datetime': forecast['dt_txt'],
				'temperature': forecast['main']['temp'],
				'weather': forecast['weather'][0]['description'],
				'icon_url': f"http://openweathermap.org/img/wn/{forecast['weather'][0]['icon']}@2x.png"
			}
			forecast_data.append(info)		#this is to update the list with only relevant data
			count+=1
		else:
			break
	return forecast_data