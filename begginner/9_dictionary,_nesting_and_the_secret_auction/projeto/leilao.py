
# TODO -1: Ask  the user for input
# TODO -2: Save data into dictionary {name: price}
# TODO -3: Whether if new bids need to be added
# TODO -4: Compare bids in dictionary

print(r'''              
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\      
      
                                                     ''')

# Imprime uma mensagem de boas-vindas ao usuário
print("Welcome to the secret auction program.\n")

# ===============================
# Função para encontrar o maior lance
# ===============================
def find_highest_bidder(bidding_dictionary):
    # Variável para armazenar o nome do vencedor
    winner = ""
    # Variável para armazenar o maior lance encontrado até o momento
    highest_bid = 0

    # Loop através de cada pessoa (chave) no dicionário de lances
    for bidder in bidding_dictionary:
        # Recupera o valor do lance feito pela pessoa
        bid_amount = bidding_dictionary[bidder]

        # Se esse lance for maior do que o maior lance atual, atualiza
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # atualiza o maior lance
            winner = bidder           # atualiza o nome do vencedor

    # Após verificar todos, exibe o vencedor e o valor do maior lance
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# ===============================
# Início do programa principal
# ===============================

# Dicionário para armazenar os lances: {nome: valor_do_lance}
bids = {}

# Variável de controle para saber se devemos continuar coletando lances
continue_bidding = True

# Loop que continua até que o usuário diga que não há mais lances
while continue_bidding:
    # Solicita o nome do usuário
    name = input("What is your name? ")

    # Solicita o valor do lance e converte para float
    price = float(input("What is your bid? $"))

    # Salva o nome e o valor no dicionário de lances
    bids[name] = price

    # Pergunta se há mais participantes
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    # Se não há mais participantes, finaliza o loop e exibe o vencedor
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    # Se ainda há participantes, "limpa" a tela (simulado imprimindo várias linhas em branco)
    elif should_continue == 'yes':
        print("\n" * 20)
