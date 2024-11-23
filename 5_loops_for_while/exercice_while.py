import random

# Gera um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativas = 0
adivinhou = False

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 100. Tente adivinhar!\n")

while not adivinhou:
    # Solicita ao usuário um palpite
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1  # Incrementa o número de tentativas
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        adivinhou = True
    elif palpite < numero_secreto:
        print("O número é maior! Tente novamente.")
    else:
        print("O número é menor! Tente novamente.")
