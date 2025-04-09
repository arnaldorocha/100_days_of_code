# Importa o módulo random, que será usado para escolher uma palavra aleatória.
import random

# Lista com as diferentes fases do boneco da forca, usadas para representar visualmente o número de vidas restantes.
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

# Lista de palavras possíveis para o jogo.
word_list = ['banana', 'camisa', 'uva', 'cacau', 'mãe', 'abacaxi', 'carro']

# Define o número inicial de vidas (tentativas).
lives = 6

# Escolhe aleatoriamente uma palavra da lista.
chosen_word = random.choice(word_list)

# Armazena o comprimento da palavra escolhida.
word_length = len(chosen_word)

# Cria o espaço inicial com underscores para representar cada letra da palavra.
placeholder = ' _ ' * word_length

# Exibe os espaços em branco no início do jogo.
print(placeholder)

# Variável para controlar se o jogo acabou.
game_over = False

# Lista para armazenar as letras corretas já adivinhadas.
correct_letters = []

# Loop principal do jogo, que continuará até o jogo acabar.
while not game_over: 
    print(f"***************************{lives}/6 LIVES LEFT***************************")
    
    # Solicita ao usuário que digite uma letra e converte para minúscula.
    guess = input('Guess a letter: ').lower()

    # Verifica se a letra já foi adivinhada anteriormente.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Inicializa a string que será exibida ao usuário a cada rodada.
    display = ''

    # Percorre cada letra da palavra secreta para atualizar o display.
    for letter in chosen_word:
        if letter == guess:
            # Se o chute está correto, mostra a letra.
            display += letter
            correct_letters.append(guess)  # Adiciona à lista de letras corretas.
        elif letter in correct_letters:
            # Se a letra já foi adivinhada anteriormente, continua exibindo.
            display += letter
        else:
            # Caso contrário, mantém o espaço em branco.
            display += ' _ '

    # Mostra o progresso atual da palavra.
    print(display)

    # Se o chute não estiver na palavra, perde uma vida.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print(F"***************************IT WAS {chosen_word} YOU LOSE***************************")

    # Verifica se não há mais underscores, ou seja, a palavra foi completamente descoberta.
    if "_" not in display:
        game_over = True
        print("***************************YOU WIN***************************")

    # Exibe o estágio atual da forca com base nas vidas restantes.
    print(stages[lives])
