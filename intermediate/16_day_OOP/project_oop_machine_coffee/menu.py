class MenuItem:
    """Representa uma bebida do menu."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Gerencia a lista de bebidas disponíveis."""
    def __init__(self):
        # Cria uma lista com os itens disponíveis no menu
        self.menu = [
            MenuItem("latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem("espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem("cappuccino", water=250, milk=100, coffee=24, cost=3.0),
        ]

    def get_items(self):
        """Retorna uma string com os nomes das bebidas disponíveis, separados por '/'."""
        options = [item.name for item in self.menu]
        return "/".join(options)

    def find_drink(self, order_name):
        """Procura uma bebida pelo nome digitado. Retorna o objeto MenuItem se encontrar."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Desculpe, essa bebida não está no cardápio.")
        return None
