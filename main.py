from decimal import Decimal

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
    "water": 500,
    "milk": 500,
    "coffee": 200,
}


# Check if the coffee machine has enough resources
def check_resources(drink):
    selected_drink = MENU[drink]['ingredients']
    for item, qty in selected_drink.items():
        if resources[item] < selected_drink[item]:
            return False
    return True


# Add up the coins
def check_money(pennies_qty, nickles_qty, dimes_qty, quarters_qty):
    pennies = 0.01 * pennies_qty
    nickles = 0.05 * nickles_qty
    dimes = 0.10 * dimes_qty
    quarters = 0.25 * quarters_qty

    value = round(pennies + nickles + dimes + quarters, 2)
    return value


# Check if there is enough money for coffee
def check_transaction(user_choice, value):
    choice_amnt = round(MENU[user_choice]['cost'], 2)
    if Decimal(value) < Decimal(choice_amnt):
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    change = round(value - choice_amnt, 2)
    if change != 0:
        print(f'Here is ${change} in change.')

    if 'money' in resources:
        current_money = resources['money']
        resources['money'] = current_money + choice_amnt
    else:
        resources['money'] = choice_amnt
    return True


# Reduce coffee machine resources after selling a coffee
def reduce_resources(user_choice):
    selected_drink = MENU[user_choice]['ingredients']
    for item, qty in selected_drink.items():
        resources[item] = resources[item] - selected_drink[item]


while True:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')

    if user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        if 'money' in resources:
            print(f"Money: ${resources['money']}")
            continue

    elif user_choice == 'off':
        break

    elif not check_resources(user_choice):
        print("Sorry, but the machine has ran out of coffee :(")
        break

    else:
        coffee_price = round(MENU[user_choice]['cost'], 2)
        print(f'Price of {user_choice} is ${coffee_price}')
        print('Please insert coins.')
        quarters_qty = float(input('How many quarters?: '))
        dimes_qty = float(input('How many dimes?: '))
        nickles_qty = float(input('How many nickles?: '))
        pennies_qty = float(input('How many pennies?: '))

        value = check_money(pennies_qty, nickles_qty, dimes_qty, quarters_qty)
        if check_transaction(user_choice, value):
            reduce_resources(user_choice)
            print(f'Here is your {user_choice} ☕. Enjoy!')
        