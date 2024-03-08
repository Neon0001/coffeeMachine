from recipes import MENU

profit = 0
resources = {
    "water": 300,
    "milk": 300,
    "coffee": 100
}


def is_resources_enough(customer_c_ingredients):
    for item in customer_c_ingredients:
        if customer_c_ingredients[item] >= resources[item]:
            print("Sorry, there is not enough ingredients.")
            return False
        else:
            return True


def process_coins():
    print("Please Insert Coins")
    total = int(input("Insert quarter: ")) * 0.25
    total += int(input("Insert dimes: ")) * 0.10
    total += int(input("Insert nickles: ")) * 0.05
    total += int(input("Insert Penny: ")) * 0.01
    return total


def was_transaction_accepted(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Your change is: {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Money wasn't enough. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print(f"Here's your {drink_name}")


machine_on = True


while machine_on:
    customer_order = input("What would you like to buy: espresso/latte/cappuccino ")
    if customer_order == "off":
        machine_on = False
    elif customer_order == "report":
        print(f"water:{resources['water']}")
        print(f"milk:{resources['milk']}")
        print(f"coffe:{resources['coffee']}")
        print(f"money:${profit}")
    else:
        drink = MENU[customer_order]
        if is_resources_enough(drink["ingredients"]):
            payment = process_coins()
            if was_transaction_accepted(payment, drink['cost']):
                make_coffee(customer_order, drink['ingredients'])




