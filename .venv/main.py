import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker.SandwichMaker(resources, recipes)
cashier_instance = Cashier.Cashier(sandwich_maker_instance)

def main():
    while True:
        print("What would you like? (small/ medium/ large/ off/ report): large")
        input = input()
        if input == "large":
            if (sandwich_maker_instance.check_resources(recipes["large"])):
                total = cashier_instance.process_coins()
                if (cashier_instance.transaction_result(total, recipes["large"]["cost"])):
                    sandwich_maker_instance.make_sandwich("large", recipes)
                    print("large sandwich is ready. Bon appetit!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough ingredients")
        elif input == "medium":
            if (sandwich_maker_instance.check_resources(recipes["medium"])):
                total = cashier_instance.process_coins()
                if (cashier_instance.transaction_result(total, recipes["medium"]["cost"])):
                    sandwich_maker_instance.make_sandwich("medium", recipes)
                    print("medium sandwich is ready. Bon appetit!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough ingredients")
        elif input == "small":
            if (cashier_instance_instance.check_resources(recipes["small"])):
                total = cashier_instance.process_coins()
                if (machine.transaction_result(total, recipes["small"]["cost"])):
                    sandwich_maker_instance.make_sandwich("small", recipes)
                    print("small sandwich is ready. Bon appetit!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough ingredients")
        elif input == "off":
            exit(1)
        elif input == "report":
            print("Bread: ", sandwich_maker_instance.machine_resources["bread"])
            print("Ham: ", sandwich_maker_instance.machine_resources["ham"])
            print("Cheese: ", sandwich_maker_instance.machine_resources["cheese"])
        else:
            print("Error Invalid input")

if __name__=="__main__":
    main()