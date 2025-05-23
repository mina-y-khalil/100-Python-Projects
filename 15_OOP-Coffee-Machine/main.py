from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#using the blueprint of the classes and assign it to new variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

money_machine.report()
coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like {options}: ")
    if choice == "off":
        is_on = False
        print ("Turning off the machine ... 😴")