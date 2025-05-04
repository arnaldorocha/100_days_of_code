import requests
from datetime import *

MY_LAT = -25.924702
MY_LONG = -51.895042

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="httpS://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()

# sunrise = data['results']['sunrise']
# sunset = data['results']['sunset']

# print(sunrise)
# print(sunrise.split("T"))
# print(sunrise.split("T")[1].split(":"))
# print(sunrise.split("T")[1].split(":")[0])

sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)


time_now = datetime.now()

# print(time_now)
print(time_now.hour )