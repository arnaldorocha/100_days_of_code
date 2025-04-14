# Fingir ser um computador lendo um código, e dando resposta referente ao código

year = int(input("What's your year of birth?"))

if year >= 1980 and year <= 1994:    # na lógica  não tem o valor igual
    print("You are a millennial.") # da bug por que se digitar 1994 ou 1980 nao imprime nada
elif year > 1994:
    print("You are a Gen Z.")

      