import requests 

key_api = "a1b7579d847c4cae5da2a6b1d7bbc937"

#url ver tempo no parana
#url2 ver tempo da minha cidade
url = "https://api.openweathermap.org/data/2.5/weather?q=parana,br&appid=a1b7579d847c4cae5da2a6b1d7bbc937"  # variavel pra ler api
url2 = "https://api.openweathermap.org/data/2.5/weather?lat=-25.896696&lon=-50.376738&appid=a1b7579d847c4cae5da2a6b1d7bbc937"

response = requests.get(url)
response2 = requests.get(url2)

data = response.json() 
data2 = response2.json() 

print(data)
print("\n\n\n")
print(data2)