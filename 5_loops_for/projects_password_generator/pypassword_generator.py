import random

# Geração de caracteres
letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]  # Letras minúsculas (a-z) e maiúsculas (A-Z)
numbers = [str(i) for i in range(0, 10)]  # Números de '0' a '9'
symbols = ''.join(chr(i) for i in range(33, 48)) + \
          ''.join(chr(i) for i in range(58, 65)) + \
          ''.join(chr(i) for i in range(91, 97)) + \
          ''.join(chr(i) for i in range(123, 127))

print('Welcome to the PyPassword Generator!\n')

# Coletar as preferências do usuário
n_letters = int(input('How many letters (both uppercase and lowercase) would you like in your password? '))
n_symbols = int(input('How many symbols would you like? '))
n_numbers = int(input('How many numbers would you like? '))

# Geração da senha
password = []

# Adiciona letras, símbolos e números à senha
password += random.choices(letters, k=n_letters)  # Letras maiúsculas e minúsculas
password += random.choices(symbols, k=n_symbols)  # Símbolos
password += random.choices(numbers, k=n_numbers)  # Números

# Embaralha os caracteres para maior segurança
random.shuffle(password)

# Converte a lista de caracteres em uma string final
final_password = ''.join(password)

print(f'Your password is: {final_password}')
