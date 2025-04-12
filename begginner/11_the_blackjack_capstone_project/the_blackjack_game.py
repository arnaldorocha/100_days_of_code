import random

# Logo do jogo (só visual)
logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Função para sortear uma carta aleatória
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]  # 11 é o Ás, os 10s representam 10, J, Q e K
    return random.choice(cards)

# Função para calcular a pontuação atual da mão
def calculate_score(cards):
    # Se tiver duas cartas que somam 21 → é um Blackjack!
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Zero representa Blackjack

    # Se tiver Ás (11) e a pontuação passar de 21, converte o Ás em 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

# Função para comparar os resultados do jogador e do computador
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Empate! 🤝"
    elif computer_score == 0:
        return "Você perdeu, o computador fez Blackjack! 😱"
    elif user_score == 0:
        return "Parabéns! Você fez Blackjack! 🥳"
    elif user_score > 21:
        return "Você estourou! 😢"
    elif computer_score > 21:
        return "O computador estourou. Você venceu! 🎉"
    elif user_score > computer_score:
        return "Você venceu! 😄"
    else:
        return "Você perdeu! 😩"

# Função principal do jogo
def play_game():
    print(logo)
    
    # Listas para armazenar as cartas
    user_cards = []
    computer_cards = []

    # Distribui duas cartas para cada jogador
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nSuas cartas: {user_cards}, Pontuação: {user_score}")
        print(f"Carta revelada do computador: {computer_cards[0]}")

        # Verifica se alguém já ganhou/perdeu logo de cara
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Pergunta ao jogador se ele quer mais uma carta
            user_should_continue = input("Digite 's' para comprar mais uma carta ou 'n' para parar: ")
            if user_should_continue == "s":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computador compra cartas até ter pelo menos 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Mostrar resultado final
    print(f"\nSuas cartas finais: {user_cards}, pontuação: {user_score}")
    print(f"Cartas do computador: {computer_cards}, pontuação: {computer_score}")
    print(compare(user_score, computer_score))

# Pergunta se o jogador quer jogar novamente
while input("Quer jogar uma partida de Blackjack? Digite 's' ou 'n': ") == "s":
    play_game()
