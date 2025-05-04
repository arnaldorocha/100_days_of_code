import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response) #código de reposta, como o código resposta 404 
print(response.status_code)
#1xx hold on, 2xx here you go, 3xx go away, 4xx you screwed up, 5xx I screwed up
response.raise_for_status() #execptions error referente ao status code

data = response.json()  #igual o browser
print(data)  


# data = response.json()['iss_position']['longitude'] #conchete seleciona os valores especifico do dicionario
# print(data)  

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

print(iss_position)