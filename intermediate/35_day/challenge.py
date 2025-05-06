

# Previsão de tempo de 5 dias e localizar a previsao de tempo na resposta JSON que voce receber de volta

import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# 1 TODO: Get your latitude and longitude from latlong.net
#lat=-25.896696&lon=-50.376738

api_key = "a1b7579d847c4cae5da2a6b1d7bbc937"


weather_params = {
    "lat":-25.868136,
    "lon":-50.393960,
    "appid": api_key,
}

# 2 TODO: Make a request to the forecast api using the request module

response = requests.get(OWN_Endpoint, params=weather_params)
print(response.json())

# 3 TODO: Print out the HTTP status code that you get back.

# 4 TODO: Print the response to the console

# 5 TODO: Copy-paste the response to an online JSON viewer

# 6 TODO: Locate the weather id and description for each forecast 