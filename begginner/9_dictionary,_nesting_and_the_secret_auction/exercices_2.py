dicionario_inicial = { 
    "a" : 9 , 
    "b" : 8 , 
}


dicionario_final = { 
    "a" : 9 , 
    "b" : 8 , 
    "c" : 7 , 
}

dicionario_inicial["c"] = 7
dicionario_final = dicionario_inicial

print(dicionario_inicial)

for dicionario in dicionario_inicial:
    print(f'{dicionario} : {dicionario_inicial[dicionario]}' )


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key] += 1
print(dict)

dict['c'] = [1,2,3]

print(dict)

dict[1] = 4
dict[2] = 5
dict['d'] = 6


print(dict)