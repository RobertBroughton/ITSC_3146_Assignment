class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        return self.bread >= ingredients["bread"] & self.ham >= ingredients["ham"] & self.cheese >= ingredients["cheese"]

    def make_sandwich(self, sandwich_size, order_ingredients):
        self.bread -= order_ingredients[sandwich_size]["bread"]
        self.ham -= order_ingredients[sandwich_size]["ham"]
        self.cheese -= order_ingredients[sandwich_size]["cheese"]