from coffee_menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from coffee_money import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

drink = True

while drink == True:
    print()
    want = input("What do you want? espresso? latte? cappuccino? report? stop? ")
    print()
    if want == "report":
        print(money.report())
        print(maker.report())
    elif want == "stop":
        drink = False
    else:
        if maker.is_resource_sufficient(menu.find_drink(want)) == True:
            item = menu.find_drink(want)
            print(f"This drink costs {item.cost}")
            if money.make_payment(item.cost) == True:
                maker.make_coffee(item)
