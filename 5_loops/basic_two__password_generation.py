import random

letters = ['a','b','c','d','e','f', 'g', 'h', 
           'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 
           'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5','6','7','8','9']
symbols = ['!','#','$','%','&','*','(',')','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in you password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Easy level
# password = ""

# for char in range(0, nr_letters):
#     password += random.choice(letters)
    
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# print(password)

# Hard level
  
password_list = []

for char in range( nr_letters):
    password_list.append(random.choice(letters))
    
for char in range( nr_numbers):
    password_list.append(random.choice(numbers))

for char in range( nr_symbols):
    password_list.append(random.choice(symbols))

print(f"{password_list}\n")
random.shuffle(password_list)
print(f"{password_list}\n")

password = ""

for char in password_list:
    password += char

print(f"{password} \n")