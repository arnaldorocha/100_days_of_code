class CoffeeMaker:
    """Gerencia os recursos da máquina e prepara o café."""

    def __init__(self):
        # Define os ingredientes iniciais
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Exibe o relatório atual de recursos disponíveis."""
        print(f"\nÁgua: {self.resources['water']}ml")
        print(f"Leite: {self.resources['milk']}ml")
        print(f"Café: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Verifica se há recursos suficientes para preparar a bebida."""
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Desculpe, não há {item} suficiente.")
                return False
        return True

    def make_coffee(self, order):
        """Deduz os ingredientes usados e 'serve' a bebida."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"☕ Aqui está seu {order.name}. Aproveite!\n")
