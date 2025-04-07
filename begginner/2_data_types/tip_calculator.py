print("Bem vindo a calculadora de gorjeta e divisão de quanto cada um deve pagar \n")

comida = float(input("\nQual foi o valor da comida? "))
porcentagem_gorjeta = float(input("\nQual foi o valor da gorjeta referente a porcentagem da comida? "))
pessoas = int(input("\nQuantas pessoas vão pagar a gorjeta? "))

porcentagem = comida / 100 
gorjeta = porcentagem * porcentagem_gorjeta 
gorjeta_por_pessoa = gorjeta / pessoas 
div_comida = comida / pessoas
total = div_comida + gorjeta_por_pessoa

print(f'\nCada pessoa vai pagar {round(gorjeta_por_pessoa, 2)} de gorjeta\n')
print(f'Cada pessoa vai pagar pela comida R${round(div_comida, 2)}\n')
print(f'Cada pessoa vai pagar pela comida + gorjeta R${round(total, 2)}\n')