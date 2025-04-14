# Usamos o bloco try para tentar executar um código que pode gerar erro
try:
    # Aqui pedimos ao usuário que digite sua idade
    # A função input() sempre retorna uma string, então usamos int() para converter para número inteiro
    age = int(input("How old are you?"))
    
# Caso o usuário digite algo que não possa ser convertido para inteiro (como letras), ocorre um erro do tipo ValueError
except ValueError:
    # Informamos ao usuário que ele digitou algo inválido
    print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
    # Pedimos novamente a idade, esperando que agora ele digite um número válido
    # OBS: Se o usuário errar novamente aqui, o programa irá encerrar com erro porque não há outro try
    age = int(input("How old are you?"))

# Verificamos se a idade informada é maior que 18
if age > 18:
    # Se for, mostramos uma mensagem dizendo que a pessoa pode dirigir
    # O f-string permite incluir variáveis dentro da string de forma prática
    print(f"You can drive at age {age}.")
else:
    print(f"Nao pode digirir faça uma carteira")