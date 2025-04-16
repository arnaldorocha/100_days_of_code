from menu_coffee import MENU, resources

profit = 0.0


def is_resource_sufficient(order_ingredients):
    """Verifica se há ingredientes suficientes para o pedido."""
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Desculpe, não há {item} suficiente.")
            return False
    return True

def process_coins(drink_cost):
    """Calcula o valor inserido pelas moedas, com validação."""
    print(f"O valor do café é: ${drink_cost}")
    print("Por favor, insira as moedas.")

    total = 0.0
    coin_types = {
        "quarters (25¢)": 0.25,
        "dimes (10¢)": 0.10,
        "nickels (5¢)": 0.05,
        "pennies (1¢)": 0.01,
    }

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
                print("Entrada inválida. Digite apenas números ou deixe em branco.")

    total = round(total, 2)
    print(f"Total inserido: ${total}")
    return total

def is_transaction_successful(money_received, drink_cost):
    """Verifica se o pagamento foi suficiente."""
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Aqui está seu troco: ${change}")
        profit += drink_cost
        return True
    else:
        print("Dinheiro insuficiente. Dinheiro devolvido.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Prepara o café e atualiza os recursos."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Aqui está seu {drink_name} ☕. Aproveite!")


def print_report():
    """Exibe o relatório de recursos e lucro."""
    print("\n📊 RELATÓRIO:")
    print(f"Água: {resources['water']}ml")
    print(f"Leite: {resources.get('milk', 0)}ml")
    print(f"Café: {resources['coffee']}g")
    print(f"Lucro: ${profit}\n")


def refill_resources():
    """Permite reabastecer ingredientes manualmente."""
    print("\n🔁 Reabastecendo recursos...")
    for item in resources:
        try:
            amount = int(input(f"Adicionar quanto de {item}? "))
            resources[item] += amount
        except ValueError:
            print("Valor inválido. Pulando esse item.")
    print("✅ Recursos atualizados.\n")


def main():
    is_on = True
    while is_on:
        print("Menu: espresso / latte / cappuccino / report / refill / off")
        choice = input("O que você gostaria? ").lower()

        if choice == "off":
            print("☕ Máquina desligada. Até logo!")
            is_on = False
        elif choice == "report":
            print_report()
        elif choice == "refill":
            refill_resources()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins(drink["cost"])
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
                    continuar = input("Deseja outro café? (s/n): ").lower()
                    if continuar == "n":
                        print("☕ Obrigado por usar a máquina de café. Até logo!")
                        is_on = False

        else:
            print("❌ Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
