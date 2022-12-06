MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}


def print_report():
    output = f"water: {resources['water']}ml\n"
    output += f"milk: {resources['milk']}ml\n"
    output += f"coffee: {resources['coffee']}g\n"
    output += f"money: ${resources['money']}\n"
    print(output)


def collect_money(selection : str):
    money: float = 0
    for coin, value in zip(('quarters', 'dimes', 'nickles', 'pennies'), (0.25, 0.10, 0.5, 0.1)):
        try:
            money += value * int(input(f"how many {coin}?:"))
        except ValueError:
            pass
    return money


def sufficient_ingredients(selection: str) -> bool:
    for ingredient, amount in MENU[selection]['ingredients'].items():
        if amount > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        return True

def get_coffee(selection):
    """
    :type selection: str
    """
    for ingredient, amount in MENU[selection]['ingredients'].items():
        resources[ingredient] -= amount
    resources['money'] += MENU[selection]['cost']
    print(f"Here is your {selection}. Enjoy!")


def process_selection():
    """
    Asks for input and processes the selection
    :type input_resources: str
    :rtype: dict 
    """
    is_on = True
    while is_on:
        selection: str = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if selection == 'report':
            print_report()
        elif selection in ['espresso', 'latte', 'cappuccino']:
            cost = MENU[selection]['cost']
            print(f"{selection} is ${cost}. Insert coins now.")
            if sufficient_ingredients(selection):
                money: float = collect_money(selection)
                if money >= cost:
                    get_coffee(selection)
                    if money > cost:
                        print(f"Here is ${money - cost} in change.")
                else:
                    print(f"Sorry that is not enough money. Here is your ${money} back")
        elif selection == 'off':
            is_on = False
        else:
            print("Selection not known. Go again...")
            process_selection()


process_selection()

