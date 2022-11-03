import requests
from pynotifier import Notification

key = "8633dfbc490a72a27d9a540213feb8ad"
url = "https://api.openweathermap.org/data/2.5/weather?q="
name = "riverside"

data = requests.get(url + name + '&appid=' + key).json()
# data = requests.request("GET", url, headers=headers, params=querystring)
city = data['name']
country = data['sys']['country']
temperature = (data['main']['temp_max'] - 273.15) * (9/5) + 32
weather = data['weather'][0]['main']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

if data['cod'] != '404':
    Notification(title = city+', '+country, 
                 description = f'{temperature}F {weather}\n Humidity: {humidity} \n Pressure: {pressure}',
                 duration = 5).send()
else:
    print("City not found")
    