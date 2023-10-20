logo ='''

 _______  _______  _______  _______  _______  _______    __   __  _______  _______  __   __  ___   __    _  _______ 
|       ||       ||       ||       ||       ||       |  |  |_|  ||   _   ||       ||  | |  ||   | |  |  | ||       |
|       ||   _   ||    ___||    ___||    ___||    ___|  |       ||  |_|  ||       ||  |_|  ||   | |   |_| ||    ___|
|       ||  | |  ||   |___ |   |___ |   |___ |   |___   |       ||       ||       ||       ||   | |       ||   |___ 
|      _||  |_|  ||    ___||    ___||    ___||    ___|  |       ||       ||      _||       ||   | |  _    ||    ___|
|     |_ |       ||   |    |   |    |   |___ |   |___   | ||_|| ||   _   ||     |_ |   _   ||   | | | |   ||   |___ 
|_______||_______||___|    |___|    |_______||_______|  |_|   |_||__| |__||_______||__| |__||___| |_|  |__||_______|

'''
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def input_quantity():
    quantity = int(input('input the quantity you want to add : '))
    return  quantity
def add_resources_fun():
    choice = input ('witch resource you want to add (water\ milk\ coffee)')
    resources[choice] += input_quantity()
    print('your resources now is : ')
    report_fun()
def remove_the_quantity_fun(demand):
    global profit
    M = MENU[demand]['ingredients']
    for i in M:
         resources[i] = resources[i] - M[i]
    profit += MENU[demand]["cost"]
def check_resources_sufficient_fun(demand):
    M = MENU[demand]['ingredients']
    for i in M :
        if M[i] > resources[i] :
            return False
    return  True
def report_fun():
    for i in resources:
        print (f'{i} : {resources[i]}')
    print(f'Money : {profit}')
    input('')
def insert_coins_fun():
    quarters = int(input('How many quarters? : '))
    dimes = int(input('How many dimes? : '))
    nickles = int(input('How many nickles? : '))
    pennies = int(input('How many pennies? : '))
    return  quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
def demand_fun(demand):
    if check_resources_sufficient_fun(demand):
        payed = round(insert_coins_fun(), 2)
        print(f'Been paid: ${payed} and  the ${demand} price: {MENU[demand]["cost"]}')
        if payed >= MENU[demand]['cost'] :
            print(f'Here is your {demand} Enjoy!')
            remove_the_quantity_fun(demand)
        else:
            print(f'Sorry there is not enough money, you need ${round(MENU[demand]["cost"]-payed,2)}. Money refunded')
    else:
        print(f'Sorry there is not enough resources')
def demand_espresso_fun():
     demand_fun('espresso')
def demand_latte_fun():
     demand_fun('latte')
def demand_cappuccino_fun():
     demand_fun('cappuccino')
def coffee_machine_fun():
    try:
        print ( logo)
        choice_input = input('What would you like? (espresso/ latte/ cappuccino) : ')
        dic_coices = {
            'espresso':demand_espresso_fun,
            'latte':demand_latte_fun,
            'cappuccino':demand_cappuccino_fun,
            'report':report_fun,
            'add': add_resources_fun
        }
        if choice_input == 'exit':
            print('see you in the next time ')
        else:
            dic_coices[choice_input]()
            coffee_machine_fun()
    except :
        coffee_machine_fun()
coffee_machine_fun()
