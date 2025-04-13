def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Entrada do usuário
num = int(input("Digite um número: "))

# Verificação e saída
if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
