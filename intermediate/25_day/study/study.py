# with open(".100_days/Intermediate/25_day/weather_data.csv") as names_file:
#     names = names_file.readlines()

# import csv

# with open("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != " temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas 

pandas_data = pandas.read_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/study/weather_data.csv")
# print(pandas_data[" temp"])

# data_dict = pandas_data.to_dict()
# # print(data_dict)

# media = pandas_data[" temp"].mean()
# print(media)
# print(pandas_data[" temp"].mean())

# print(pandas_data[" temp"].max()) #VER NA DOCUMENTAÇÃO DO PANDAS COMO FAZER ISSO

# print(pandas_data[" temp"].to_list()) #VER NA DOCUMENTAÇÃO DO PANDAS COMO FAZER ISSO
# to_list = pandas_data[" temp"].to_list()
# print(to_list)

# #Get data in columns [' condition'] and ['day']
# print(pandas_data["condition"].to_list()) #VER NA DOCUMENTAÇÃO DO PANDAS COMO FAZER ISSO

# #Get data in row [0] and [1]
# print(pandas_data["condition"][0]) #VER NA DOCUMENTAÇÃO DO PANDAS COMO FAZER ISSO
# print(pandas_data[pandas_data.day == "Monday"])
# print(pandas_data[pandas_data.condition == "Rainy"])
# print(pandas_data[pandas_data.condition == "Rainy"].day) #VER NA DOCUMENTAÇÃO DO PANDAS COMO FAZER ISSO

# print(pandas_data[pandas_data.temp == pandas_data.temp.max()]) #VER linha com maior temperatura
# print(pandas_data[pandas_data.temp == pandas_data.temp.max()]["day"]) #VER dia com maior temperatura
# print(pandas_data[pandas_data.temp == pandas_data.temp.max()]["condition"]) #VER condição com maior temperatura
# print(pandas_data[pandas_data.temp == pandas_data.temp.max()]["temp"]) #VER temperatura com maior temperatura

print(f'Temperadura em celsius: {pandas_data[pandas_data.day == "Monday"].temp[0]}') #VER temperatura de segunda-feira

c = pandas_data[pandas_data.day == "Monday"].temp[0]
f = (c * 9/5) + 32
 #VER temperatura de segunda-feira em Fahrenheit
print(f"Temperatura de segunda-feira em Fahrenheit: {f}")