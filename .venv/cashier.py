class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        total = 0
        total += input("how many large dollars?: ")
        total += (input("how many half dollars?: ") * .5)
        total += (input("how many quarters?: ") * .25)
        total += (input("how many nickles?: ") * .05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        return coins >= cost