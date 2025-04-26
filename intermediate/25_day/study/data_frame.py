import pandas as pd

#creating a data frame from scratch

data_dict = {
    "Student": ["Angela", "James", "Lily"],
    "Score": [56, 76, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("c:/Users/arnal/OneDrive/Área de Trabalho/Python_Way/100_days_of_code/intermediate/25_day/study/new_data.csv", index=False) 