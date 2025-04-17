class MoneyMachine:
    """Gerencia o pagamento e calcula o lucro."""

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,  # 25 centavos
        "dimes": 0.10,     # 10 centavos
        "nickles": 0.05,   # 5 centavos
        "pennies": 0.01,   # 1 centavo
    }

    def __init__(self):
        self.profit = 0     # Lucro total da máquina
        self.money_received = 0

    def report(self):
        """Mostra o total de dinheiro arrecadado."""
        print(f"Lucro: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Solicita ao usuário que insira moedas e calcula o total."""
        print("Por favor, insira as moedas:")
        total = 0
        for coin in self.COIN_VALUES:
            try:
                count = int(input(f"Quantas {coin}? "))
            except ValueError:
                print("Entrada inválida. Considerando 0.")
                count = 0
            total += count * self.COIN_VALUES[coin]
        return round(total, 2)

    def make_payment(self, cost):
        """Verifica se o pagamento é suficiente e calcula o troco."""
        print(f"O café custa: {self.CURRENCY}{cost}")
        payment = self.process_coins()

        if payment >= cost:
            change = round(payment - cost, 2)
            if change > 0:
                print(f"Aqui está seu troco: {self.CURRENCY}{change}")
            self.profit += cost
            return True
        else:
            print("Dinheiro insuficiente. Dinheiro devolvido.")
            return False
