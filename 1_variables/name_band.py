print("Welcome to the Band Name Generator.\n")
print("Band names that mix your pet's name and your star sign.\n")

zodiac = input("What is your Zodiac sign? ")

pet= input("What is your pet's name? ")

name = zodiac + pet

print("")

print("O nome da sua banda é: " + pet + zodiac + "\n")

print(f"o nome é {name.title()}")