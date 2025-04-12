import random

# Logo do jogo
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

# Dicionário que liga valor da carta ao nome visual
cards_dict = {
    11: "A♠️", 2: "2♠️", 3: "3♠️", 4: "4♠️", 5: "5♠️", 6: "6♠️",
    7: "7♠️", 8: "8♠️", 9: "9♠️", 10: "10♠️ / J♠️ / Q♠️ / K♠️"
}

# Função que sorteia uma carta aleatória (valor)
def deal_card():
    card_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(card_values)

# Função que mostra as cartas de forma mais visual usando o dicionário
def display_cards(card_list):
    return [cards_dict[value] for value in card_list]

# Função que calcula a pontuação
def calculate_score(cards):
    # BlackJack → 2 cartas que somam 21
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Converte Ás de 11 para 1 se passar de 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Função que compara os scores e determina o vencedor
def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "Empate! 🤝"
    elif computer_score == 0:
        return "Você perdeu! O computador fez Blackjack! 🃏"
    elif user_score == 0:
        return "Parabéns! Você fez Blackjack! 🎉"
    elif user_score > 21:
        return "Você passou de 21. Você perdeu! 😭"
    elif computer_score > 21:
        return "O computador passou de 21. Você venceu! 😁"
    elif user_score > computer_score:
        return "Você venceu! 🎊"
    else:
        return "Você perdeu! 😢"

# Função principal do jogo
def play_game():
    print(logo)

    # Variáveis de dados: listas para as mãos
    user_cards = []
    computer_cards = []
    game_over = False

    # Distribui as cartas iniciais
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nSuas cartas: {display_cards(user_cards)} | Pontuação: {user_score}")
        print(f"Carta revelada do computador: {cards_dict[computer_cards[0]]}")

        # Condições para fim imediato do jogo
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("Digite 's' para comprar outra carta ou 'n' para parar: ").lower()
            if choice == 's':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Turno do computador (regra: parar se tiver 17 ou mais)
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    # Resultados finais
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nSuas cartas finais: {display_cards(user_cards)} | Pontuação: {user_score}")
    print(f"Cartas do computador: {display_cards(computer_cards)} | Pontuação: {computer_score}")
    print(compare_scores(user_score, computer_score))

# Loop para jogar várias rodadas
while input("Quer jogar uma rodada de Blackjack? (s/n): ").lower() == "s":
    play_game()
