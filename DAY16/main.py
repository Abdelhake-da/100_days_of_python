from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

# print(logo)
new_menu = Menu()
new_money_machine = MoneyMachine()
new_coffee_maker = CoffeeMaker()


def demand():
    choice_input = new_menu.find_drink(input(f'What would you like ? {new_menu.get_items()} : '))
    if choice_input != None:
        if new_coffee_maker.is_resource_sufficient(choice_input):
            if new_money_machine.make_payment(choice_input.cost):
                new_coffee_maker.make_coffee(choice_input)


while True:
    print(logo)
    dic = {
        '1': demand,
        '2': new_money_machine.report,
        '3': new_coffee_maker.report
    }
    try:
        dic[input('demand a drink (1)  / show report money machine (2) / show report coffee machine (3) : ')]()
        if input('if you want to turnoff the machine type "y" : ') == 'y':
            break
    except:
        continue
