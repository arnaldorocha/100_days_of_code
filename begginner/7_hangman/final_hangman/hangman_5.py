# Importa o módulo 'random' para escolher elementos aleatórios, neste caso, a palavra secreta.
import random

# Importa módulos personalizados:
# - module_desenho: contém os desenhos da forca em diferentes estágios (para cada número de vidas).
# - module_logo: contém o logotipo do jogo (uma arte ASCII).
# - module_word_list: contém a lista de palavras possíveis para o jogo.
import module_desenho
import module_logo
import module_word_list

# Escolhe aleatoriamente uma palavra da lista de palavras.
chosen_word = random.choice(module_word_list.word_list)

# Calcula o tamanho da palavra escolhida.
word_length = len(chosen_word)
# Cria a lista 'display' com um '_' para cada letra da palavra. Isso representa as letras que o jogador ainda não descobriu.
display = ['_' for _ in range(word_length)]

# Lista para armazenar as letras que o jogador já tentou.
guessed_letters = []

# Número inicial de vidas do jogador.
lives = 6

# Flag para controlar quando o jogo deve terminar.
game_over = False

# Exibe o logotipo do jogo no início.
print(module_logo.logo)


# Loop principal do jogo: continua enquanto o jogo não terminar.
while not game_over:
    # Exibe o desenho correspondente ao número atual de vidas.
    print(module_desenho.stages[lives])
    
    # Mostra a palavra com os espaços preenchidos com as letras já acertadas.
    print("\nPalavra: " + " ".join(display))
    
    # Mostra as letras que o jogador já tentou.
    print(f"\nLetras tentadas: {', '.join(guessed_letters)}")
    
    # Pede ao jogador para digitar uma letra.
    guess = input("\nChute uma letra: ").lower()

    # Verifica se o chute é válido (apenas uma letra do alfabeto).
    if not guess.isalpha() or len(guess) != 1:
        print("Por favor, digite apenas uma letra.")
        continue

    # Verifica se o jogador já tentou essa letra antes.
    if guess in guessed_letters:
        print(f"Você já tentou '{guess}'. Tente outra letra.")
        continue

    # Adiciona a letra chutada à lista de letras tentadas.
    guessed_letters.append(guess)

    # Verifica se a letra está presente na palavra.
    if guess in chosen_word:
        # Se estiver, percorre a palavra e revela todas as ocorrências dessa letra no 'display'.
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess

        # Se não houver mais '_' no display, o jogador venceu.
        if "_" not in display:
            game_over = True
            print("\nParabéns, você ganhou!")
    else:
        # Se a letra não estiver na palavra, o jogador perde uma vida.
        lives -= 1
        print(f"\nLetra errada! Você perdeu uma vida. Vidas restantes: {lives}")
        
        # Se as vidas chegarem a zero, o jogo termina com derrota.
        if lives == 0:
            game_over = True
            print(module_desenho.stages[0])  # Mostra o desenho final da forca.
            print(f"\nVocê perdeu! A palavra era: {chosen_word}")

# Ao final do jogo, mostra a palavra completa (com ou sem espaços).
print("\nPalavra final: " + " ".join(display))
