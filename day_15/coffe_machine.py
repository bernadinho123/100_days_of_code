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
stock = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0

}
espresso_cost = MENU['espresso']['cost']
latte_cost = MENU['latte']['cost']
cappuccino_cost = MENU['cappuccino']['cost']
flag = True

while flag:
    product = input("what would you like? (espresso/latte/cappuccino): ")
    if product == 'espresso':
        if stock['water'] < MENU['espresso']['ingredients']['water'] or stock['coffee'] \
                < MENU['espresso']['ingredients']['coffee']:
            print('Sorry, there is not enough ingredients for you espresso.')
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
            if money_inserted < espresso_cost:
                print("sorry that's not enough money.Money refunded")
            else:
                stock['money'] += espresso_cost
                change = money_inserted - espresso_cost
                print(f"Here is ${round(change, 2)} in change.")
                print("Here is your espresso ☕")
                stock['water'] -= MENU['espresso']['ingredients']['water']
                stock['coffee'] -= MENU['espresso']['ingredients']['coffee']
    elif product == 'latte':
        if stock['water'] < MENU['latte']['ingredients']['water'] or stock['coffee'] \
                < MENU['latte']['ingredients']['coffee'] or stock['milk'] < MENU['latte']['ingredients']['milk']:
            print('Sorry, there is not enough ingredients for you espresso.')
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
            stock['money'] += latte_cost
            change = money_inserted - latte_cost
            print(f"Here is ${round(change, 2)} in change.")
            print("Here is your latte ☕")
            stock['water'] -= MENU['latte']['ingredients']['water']
            stock['coffee'] -= MENU['latte']['ingredients']['coffee']
            stock['milk'] -= MENU['latte']['ingredients']['milk']
    elif product == 'cappuccino':
        if stock['water'] < MENU['cappuccino']['ingredients']['water'] or stock['coffee'] \
                < MENU['cappuccino']['ingredients']['coffee'] or stock['milk'] < MENU['cappuccino']['ingredients']['milk']:
            print('Sorry, there is not enough ingredients for you espresso.')
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            money_inserted = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
            stock['money'] += cappuccino_cost
            change = money_inserted - cappuccino_cost
            print(f"Here is ${round(change, 2)} in change.")
            print("Here is your cappuccino ☕")
            stock['water'] -= MENU['cappuccino']['ingredients']['water']
            stock['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            stock['milk'] -= MENU['cappuccino']['ingredients']['milk']
    elif product == 'report':
        print(f"water : {stock['water']}ml\nmilk : {stock['milk']}ml\ncoffe : {stock['coffee']}g\n"
              f"money : ${stock['money']}")

    elif product == 'off':
        print("turning off...")
        flag = False
    else:
        print("Error, type correctly.!")
