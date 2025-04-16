from menu_coffee import MENU, resources  # Importa cardápio e recursos

profit = 0.0  # Variável global que guarda o lucro da máquina


def is_resource_sufficient(order_ingredients):
    """
    Verifica se há ingredientes suficientes para preparar o café escolhido.
    Retorna True se sim, ou False com uma mensagem de erro se faltar algo.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Desculpe, não há {item} suficiente.")
            return False
    return True


def process_coins(drink_cost):
    """
    Exibe o valor do café e solicita ao usuário que insira moedas.
    Aceita apenas números válidos, e trata entradas vazias como 0.
    Retorna o total inserido.
    """
    print(f"\n💰 O valor do café é: ${drink_cost}")
    print("Por favor, insira as moedas:")

    total = 0.0  # Valor total inserido pelo usuário

    # Dicionário de tipos de moeda e seus valores
    coin_types = {
        "quarters (25¢)": 0.25,
        "dimes (10¢)": 0.10,
        "nickels (5¢)": 0.05,
        "pennies (1¢)": 0.01,
    }

    # Para cada tipo de moeda, solicitar a quantidade
    for coin, value in coin_types.items():
        while True:
            entrada = input(f"Quantos {coin}? ")
            if entrada == "":
                print(f"Nenhuma moeda de {coin} inserida.")
                break
            elif entrada.isdigit():
                total += int(entrada) * value
                break
            else:
                print("❌ Entrada inválida. Digite apenas números ou deixe em branco.")

    total = round(total, 2)
    print(f"💵 Total inserido: ${total}")
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Verifica se o valor recebido cobre o custo do café.
    Se sim, calcula o troco, adiciona o lucro e retorna True.
    Caso contrário, informa e devolve o dinheiro (False).
    """
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Troco: ${change}")
        profit += drink_cost
        return True
    else:
        print("Dinheiro insuficiente. Dinheiro devolvido.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    Deduz os ingredientes usados da máquina e entrega o café.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕ Aqui está seu {drink_name}. Aproveite!\n")


def print_report():
    """
    Exibe um relatório atual dos recursos e lucro.
    """
    print("\n📊 RELATÓRIO ATUAL:")
    print(f"Água: {resources['water']}ml")
    print(f"Leite: {resources.get('milk', 0)}ml")
    print(f"Café: {resources['coffee']}g")
    print(f"Lucro: ${profit}\n")


def refill_resources():
    """
    Permite reabastecer os ingredientes manualmente.
    """
    print("\n🔄 Reabastecendo ingredientes...")
    for item in resources:
        try:
            amount = int(input(f"Quanto de {item} deseja adicionar? "))
            resources[item] += amount
        except ValueError:
            print("Entrada inválida. Esse item não foi alterado.")
    print("✅ Ingredientes atualizados!\n")


def main():
    """
    Função principal que roda a máquina de café em um loop.
    Permite escolher cafés, ver relatório, reabastecer ou desligar.
    Após servir um café, pergunta se o usuário quer outro.
    """
    is_on = True

    while is_on:
        print("☕ MENU: espresso / latte / cappuccino / report / refill / off")
        choice = input("O que você gostaria? ").lower()

        if choice == "off":
            print("👋 Máquina desligada. Até logo!")
            is_on = False

        elif choice == "report":
            print_report()

        elif choice == "refill":
            refill_resources()

        elif choice in MENU:
            drink = MENU[choice]
            # Verifica se há recursos disponíveis
            if is_resource_sufficient(drink["ingredients"]):
                # Processa o pagamento
                payment = process_coins(drink["cost"])
                # Se o pagamento for suficiente, faz o café
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
                    # Pergunta se o usuário quer outro café
                    continuar = input("Deseja outro café? (s/n): ").lower()
                    if continuar == "n":
                        print("👋 Obrigado por usar a máquina de café. Até a próxima!")
                        is_on = False
        else:
            print("❌ Opção inválida. Tente novamente.\n")


# Executa o programa
if __name__ == "__main__":
    main()
