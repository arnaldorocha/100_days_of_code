# numbers = [1, 2, 3]
# squared_numbers = [number + 1 for number in numbers]

# print(squared_numbers)  # Output: [2, 3, 4]

name = "Arnaldo"
new_name = [letter for letter in name]
print(new_name)  # Output: ['A', 'r', 'n', 'a', 'l', 'd', 'o']

value = [number *2 for number in range(1, 5)]
print(value)  # Output: [1, 2, 3, 4]

names = ["Arnaldo", "Lucas", "Gustavo", "Ana", "Lu", "Leonardo"]
new_names = [name for name in names if len(name) > 6]
short_names = [name for name in names if len(name) < 4]
print(new_names)  # Output: ['Arnaldo', 'Gustavo', 'Leonardo']
print(short_names)  # Output: ['Ana', 'Lu']

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [int(n) for n in list_of_strings if int(n) % 2 == 0 ]
print(result)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)



