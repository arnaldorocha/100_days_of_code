import pandas as pd
data = pd.read_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/project/data.csv")

# print(data["Primary Fur Color"].to_list()) #VER as cores primarias dos esquilos

#print(data["Primary Fur Color"].value_counts()) #VER a quantidade de esquilos por cor primaria

grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(f'quantidade de esquilos cinzas: {grey_squirrels}') #VER a quantidade de esquilos cinzas
print(f'quantidade de esquilos vermelhos: {red_squirrels}') #VER a quantidade de esquilos vermelhos
print(f'quantidade de esquilos pretos: {black_squirrels}') #VER a quantidade de esquilos pretos

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df =pd.DataFrame(data_dict)
df.to_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/project/squirrel_count.csv", index=False) #CRIAR o arquivo csv com os dados dos esquilos