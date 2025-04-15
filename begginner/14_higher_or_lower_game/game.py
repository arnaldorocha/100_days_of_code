# Importações necessárias
import random
import os

# Arte do jogo (logo e símbolo de comparação)
logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# Dados simulando contas do Instagram com nome, seguidores, descrição e país
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    # ... (demais contas seguem aqui — mantidas no seu código original)
]

# Função que limpa a tela, compatível com Windows e Unix
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para formatar os dados da conta em uma string legível
def format_data(account):
    """Recebe os dados de uma conta e retorna uma string formatada para exibição."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

# Função que verifica se o palpite do usuário está correto
def check_answer(user_guess, a_followers, b_followers):
    """Verifica se o usuário acertou com base na quantidade de seguidores."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

# Início do jogo
score = 0
game_should_continue = True
account_b = random.choice(data)

# Loop principal do jogo
while game_should_continue:
    # A conta B da rodada anterior vira a conta A da nova rodada
    account_a = account_b
    account_b = random.choice(data)

    # Garante que as contas A e B sejam diferentes
    while account_b == account_a:
        account_b = random.choice(data)

    # Exibe o logo e as contas a serem comparadas
    clear()
    print(logo)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Usuário faz seu palpite
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Obtém os seguidores de cada conta
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Verifica se o palpite está correto
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Limpa a tela e mostra o resultado da rodada
    clear()
    print(logo)

    # Dá feedback ao jogador
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong.")
        print(f"A had {a_follower_count}M followers, B had {b_follower_count}M followers.")
        print(f"Final score: {score}.")
        game_should_continue = False
