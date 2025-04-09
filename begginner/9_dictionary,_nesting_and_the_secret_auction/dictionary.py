programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again",
}

print(programming_dictionary["Function"])

programming_dictionary["Loop"] = "The action of doing something over and over again."

empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}
print(programming_dictionary)

print('\n')

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

print('\n')

# Loop  through a dictionary
for thing in programming_dictionary:
    print(thing)

print('\n')

for key in programming_dictionary:
    print(f'{key} = {programming_dictionary[key]} \n')
 