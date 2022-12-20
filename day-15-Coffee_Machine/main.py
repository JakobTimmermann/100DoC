from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
MENU = Menu()
coffee3000 = CoffeeMaker()
donald = MoneyMachine()

def process_selection():
    """
    Asks for input and processes the selection
    """
    is_on = True
    while is_on:
        selection: str = input(f"What would you like? ({MENU.get_items()}): ").lower()
        if selection == 'report':
            coffee3000.report()
            donald.report()
        elif selection in ['espresso', 'latte', 'cappuccino']:
            drink = MENU.find_drink(selection)
            print(f"{drink.name} is ${drink.cost}.")
            if coffee3000.is_resource_sufficient(drink) and donald.make_payment(drink.cost):
                coffee3000.make_coffee(drink)
        elif selection == 'off':
            is_on = False
        else:
            print("Selection not known. Go again...")
            process_selection()


process_selection()