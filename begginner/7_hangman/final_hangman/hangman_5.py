import random

import module_desenho
import module_logo
import module_word_list

# Seleciona uma palavra aleatória
chosen_word = random.choice(module_word_list.word_list)
word_length = len(chosen_word)

# Inicializa a tela do jogo
display = ['_' for _ in range(word_length)]
guessed_letters = []
lives = 6
game_over = False

# Início do jogo
print(module_logo.logo)

while not game_over:
    print(module_desenho.stages[lives]) # <- Correto agora
    print("\nPalavra: " + " ".join(display))
    print(f"\nLetras tentadas: {', '.join(guessed_letters)}")
    
    guess = input("\nChute uma letra: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Por favor, digite apenas uma letra.")
        continue

    if guess in guessed_letters:
        print(f"Você já tentou '{guess}'. Tente outra letra.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        if "_" not in display:
            game_over = True
            print("\nParabéns, você ganhou!")
    else:
        lives -= 1
        print(f"\nLetra errada! Você perdeu uma vida. Vidas restantes: {lives}")
        if lives == 0:
            game_over = True
            print(module_desenho.stages[0])
            print(f"\nVocê perdeu! A palavra era: {chosen_word}")

print("\nPalavra final: " + " ".join(display))
