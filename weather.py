import requests

def  location():
	url = 'https://ipinfo.io/';
	res = requests.get(url)
	data = res.json()

	location = list(data['loc'].split(','))
	latitude = location[0]
	longitude = location[1]

	url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=fd05f11a6c2678132aebc007c45434ea&units=metric'.format(latitude, longitude)
	res = requests.get(url)
	data = res.json()

	temp = data['main']['temp']
	wind_speed = data['wind']['speed']
	latitude = data['coord']['lat']
	longitude = data['coord']['lon']
	description = data['weather'][0]['description']

	print("\n**************************\n")
	print('Temperature : {} degree celcius'.format(temp))
	print('Wind Speed : {} m/s'.format(wind_speed))
	print('Latitude : {}'.format(latitude))
	print('Longitude : {}'.format(longitude))
	print('Description : {}'.format(description))


def city():
	city = input('Enter City : ')
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=fd05f11a6c2678132aebc007c45434ea&units=metric'.format(city)
	res = requests.get(url)
	data = res.json()
	
	temp = data['main']['temp']
	wind_speed = data['wind']['speed']
	latitude = data['coord']['lat']
	longitude = data['coord']['lon']
	description = data['weather'][0]['description']

	print("\n**************************\n")
	print('Temperature : {} degree celcius'.format(temp))
	print('Wind Speed : {} m/s'.format(wind_speed))
	print('Latitude : {}'.format(latitude))
	print('Longitude : {}'.format(longitude))
	print('Description : {}'.format(description))

def main():
	print(' ** Weather App ** ')
	print('1. Get by City	')
	print('2. Get By Current Location')
	ch = int(input('Enter your choice : '))

	if(ch==1):
		city()
	else:
		location()


if __name__ == '__main__':
	main()
