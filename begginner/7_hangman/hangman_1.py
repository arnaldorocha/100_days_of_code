import random

 # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
 # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
 # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
 # is "Wrong" if it's not

word_list = ['banana', 'camisa', 'uva']

# TODO-1 - Escolha aleatoriamente uma palavra da word_list e atribua-a a uma variável chamada chosen_word.
# Então imprima-a.

chosen_word = random.choice(word_list)

print(chosen_word)

# TODO-2 - Peça ao usuário para adivinhar uma letra e atribua sua resposta a uma variável chamada guess. 
# Coloque guess em minúsculas.

guess = input('Guess a letter: ').lower()

# TODO-3 - Verifique se a letra que o usuário adivinhou (guess) é uma das letras da chosen_word. 
# Imprima "Right" se for certo "Wrong" se não for

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print('Wrong')

