from pprint import pp
import requests

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

pp({
    "message": "The people currently in space are: ",
    "status": people.status_code,
    "json_data": [p['name'] for p in json['people']]})

lat =  12.83
lon = 77.69
key = "830be130a6908d7f99d97cb0a84f106d"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
pp(url)
response = requests.get(url)
weather_json = response.json()

pp({"forecast": weather_json.get('weather')[0].get("main"), "temparature": f"{weather_json.get('main').get("feels_like")}°C"})