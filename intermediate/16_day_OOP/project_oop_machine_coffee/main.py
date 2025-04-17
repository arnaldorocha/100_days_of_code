# Importa as classes que representam cada parte do sistema
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Cria os objetos das classes
money_machine = MoneyMachine()     # Gerencia pagamentos
coffee_maker = CoffeeMaker()       # Gerencia os ingredientes e faz o café
menu = Menu()                      # Gerencia o cardápio e bebidas disponíveis

is_on = True  # Controla se a máquina deve continuar rodando

# Exibe o relatório inicial com os recursos da máquina
coffee_maker.report()
money_machine.report()

# Loop principal do sistema
while is_on:
    # Mostra as opções disponíveis ao usuário
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        # Encerra o programa
        is_on = False
    elif choice == "report":
        # Mostra os relatórios de recursos e dinheiro
        coffee_maker.report()
        money_machine.report()
    else:
        # Tenta encontrar a bebida escolhida no menu
        drink = menu.find_drink(choice)

        # Se a bebida existir e os recursos forem suficientes, e o pagamento for aceito:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)  # Prepara o café
