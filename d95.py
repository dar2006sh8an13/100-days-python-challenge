#weather api data fetch
import requests
city = "bengaluru"
api_key="your_api_key_here"
url="https://pro.openweathermap.org/data/2.5/forecast/climate?q={city name},{country code}&appid={API key}"
data=requests.get(url).json()
print("weather:",data["weather"][0]["description"])