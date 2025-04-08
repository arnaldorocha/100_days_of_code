import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========= ''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========= ''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========= ''', '''
  +---+
  |   |
  O   |
      |
      |
      |
========= ''', '''
  +---+
  |   |
      |
      |
      |
      |
========= ''']

word_list = ['banana', 'camisa', 'uva', 'cacau', 'mãe', 'abacaxi', 'carro']

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over: 

    print(f"***************************{lives}/6 LIVES LEFT***************************")
    guess = input('Guess a letter: ').lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(F"***************************IT WAS {chosen_word}! YOU LOSE***************************")

    if "_" not in display:
        game_over = True
        print("***************************YOU WIN***************************")

    print(stages[lives])
