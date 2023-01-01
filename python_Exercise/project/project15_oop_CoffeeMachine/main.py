from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order = Menu()
maker = CoffeeMaker()
machine = MoneyMachine()

machine_on = True 
while machine_on :
    print()
    select_coffee = input("어떤 커피를 마시겠어요?" +" ("+ order.get_items()+") : ")
    
    if select_coffee == "report" :
        maker.report()
        machine.report()
    
    elif select_coffee == "off" :
        machine_on = False
        
    else:
        if maker.is_resource_sufficient(order.find_drink(select_coffee)) :
            if machine.make_payment(order.find_drink(select_coffee).cost) :
                maker.make_coffee(order.find_drink(select_coffee))