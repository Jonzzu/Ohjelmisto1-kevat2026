import requests
import os
from dotenv import load_dotenv
load_dotenv()

city = input("Enter municipality name: ")

API_KEY = os.getenv("Open_Weather_Map_API")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

description = data["weather"][0]["description"]
temperature = data["main"]["temp"]

print(f"Weather: {description}")
print(f"Temperature: {temperature} Celsius")