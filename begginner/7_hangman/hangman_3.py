import random

word_list = ['banana', 'camisa', 'uva']
chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ''
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

game_over = False
correct_letters = []

while not game_over:
    guess = input('Guess a letter: ').lower()
    display = ''

for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(letter)
    elif letter in correct_letters:
        display += letter
    else:
        display += '_'

print(display)

if " " not in display:
    game_over = True

    print("You Win")