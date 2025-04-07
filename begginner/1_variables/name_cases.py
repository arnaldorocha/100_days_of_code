name = input("Qual o seu nome? ")
# imprime com a primeira letra maiuscula
print(f"Alô {name.title()}, você gostaria de aprender um pouco de Python?")
# imprime com as letras minuscula
print(f"Alô {name.lower()}, você gostaria de aprender um pouco de Python?")
# imprime com as letras maiusculas
print(f"Alô {name.upper()}, você gostaria de aprender um pouco de Python?")

autor = "albert einstein"
autor = autor.title()

print(f'Certa vez "{autor}" disse: "Uma pessoa que nunca cometeu um erro jamais tentou algo novo." ')

famous_person = "albert einstein"
famous_person = famous_person.title()
message = 'certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou algo novo." \t\n '

print(famous_person + " " + message)

name_text = " Rodrigo Carlos "

print(f" {name_text.strip()} " "\t\n")

print(f" {name_text.rstrip()} " "\t\n")

print(f" {name_text.lstrip()} " "\t\n")
