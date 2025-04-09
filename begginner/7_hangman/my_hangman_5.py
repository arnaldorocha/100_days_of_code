import random

# Funções para organizar o código

def exibir_status(lives, tried_letters, display, stages):
    print(f"\n{'*' * 20} {lives + 1} vidas restantes {'*' * 20}")
    print(display)
    if tried_letters:
        print("Letras tentadas:", ', '.join(sorted(tried_letters)))
    print(stages[lives])


def escolher_dificuldade():
    print("Escolha a dificuldade:")
    print("1 - Fácil (7 vidas, palavras curtas)")
    print("2 - Difícil (5 vidas, palavras longas)")
    escolha = input("Digite 1 ou 2: ")

    easy_words = ['uva', 'mãe', 'sol', 'pão', 'céu', 'lua']
    hard_words = ['abacaxi', 'camiseta', 'computador', 'bicicleta', 'floresta']

    stages_easy = ['''
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

    stages_hard = stages_easy[:5]  # Apenas 5 estágios para o modo difícil

    if escolha == '1':
        return easy_words, stages_easy, 6  # 7 vidas (0 a 6)
    elif escolha == '2':
        return hard_words, stages_hard, 4  # 5 vidas (0 a 4)
    else:
        print("Escolha inválida! Iniciando no modo fácil.")
        return easy_words, stages_easy, 6


# Início do jogo
word_list, stages, lives = escolher_dificuldade()
chosen_word = random.choice(word_list)
correct_letters = []
tried_letters = []
game_over = False

# Loop principal
while not game_over:
    # Montar a palavra com os acertos
    display = ''
    for letter in chosen_word:
        display += letter if letter in correct_letters else ' _ '

    # Mostrar status atual
    exibir_status(lives, tried_letters, display, stages)

    # Entrada do jogador
    guess = input("Digite uma letra ou a palavra completa: ").lower()

    if len(guess) > 1:
        if guess == chosen_word:
            print(f"\nParabéns! Você acertou a palavra: {chosen_word}")
            game_over = True
        else:
            lives -= 1
            print("Palavra errada! Você perdeu uma vida.")
    else:
        if guess in tried_letters:
            print(f"Você já tentou '{guess}'.")
        else:
            tried_letters.append(guess)
            if guess in chosen_word:
                correct_letters.append(guess)
                print(f"Boa! A letra '{guess}' está na palavra.")
            else:
                lives -= 1
                print(f"Letra '{guess}' não está na palavra.")

    # Verificar vitória
    if all(letter in correct_letters for letter in chosen_word):
        print(f"\nParabéns! Você descobriu a palavra: {chosen_word}")
        game_over = True

    # Verificar derrota
    if lives < 0:
        print(f"\n{stages[0]}")
        print(f"\nVocê perdeu! A palavra era: {chosen_word}")
        game_over = True
