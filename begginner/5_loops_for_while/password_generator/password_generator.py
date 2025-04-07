import random

# Geração de caracteres
letters_lower = [chr(i) for i in range(97, 123)]  # Letras minúsculas (a-z)
letters_upper = [chr(i) for i in range(65, 91)]  # Letras maiúsculas (A-Z)
numbers = [str(i) for i in range(10)]  # Números (0-9)
symbols = ''.join(chr(i) for i in range(33, 48)) + ''.join(chr(i) for i in range(58, 65)) + \
          ''.join(chr(i) for i in range(91, 97)) + ''.join(chr(i) for i in range(123, 127))

# Coletar as preferências do usuário
n_lower = int(input('How many lowercase letters? '))
n_upper = int(input('How many uppercase letters? '))
n_symbols = int(input('How many symbols? '))
n_numbers = int(input('How many numbers? '))

# Geração e embaralhamento da senha
password = random.choices(letters_lower, k=n_lower) + random.choices(letters_upper, k=n_upper) + \
           random.choices(symbols, k=n_symbols) + random.choices(numbers, k=n_numbers)
random.shuffle(password)

# Exibição da senha
print(f'Your password is: {"".join(password)}')
