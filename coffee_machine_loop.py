water_amount = 400
milk_amount = 540
beans_amount = 120
cups_count = 9
money_amount = 550

def remaining():
    print("> remaining")
    print()
    print("The coffee machine has:")
    print(water_amount, "of water")
    print(milk_amount, "of milk")
    print(beans_amount, "of coffee beans")
    print(cups_count, "of disposable cups")
    print(money_amount, "of money")
    print()

def buy():
    print("> buy")
    print()    
    global water_amount
    global milk_amount
    global beans_amount
    global cups_count
    global money_amount
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    print(">", coffee_type)
    
    
    
    if coffee_type == "1":
        if water_amount < 250:
            print("Sorry, not enough water!")
            print()
        elif beans_amount < 16:
            print("Sorry, not enough beans!")
            print()
        else:
            print("I have enough resources, making you a coffee!")
            print()    
            water_amount -= 250
            beans_amount -= 16
            money_amount += 4
            cups_count -= 1
        
    elif coffee_type == "2":
        if water_amount < 350:
            print("Sorry, not enough water!")
            print()
        elif milk_amount < 75:
            print("Sorry, not enough milk!")
            print()            
        elif beans_amount < 20:
            print("Sorry, not enough beans!")
            print()
        else:
            print("I have enough resources, making you a coffee!")
            print()
            water_amount -= 350
            milk_amount -= 75
            beans_amount -= 20
            money_amount += 7
            cups_count -= 1
            
    elif coffee_type == "3":
        if water_amount < 200:
            print("Sorry, not enough water!")
            print()
        elif milk_amount < 100:
            print("Sorry, not enough milk!")
            print()            
        elif beans_amount < 12:
            print("Sorry, not enough beans!")
            print()
        else:
            print("I have enough resources, making you a coffee!")
            print()         
            water_amount -= 200
            milk_amount -= 100
            beans_amount -= 12
            money_amount += 6
            cups_count -= 1
        
    elif coffee_type == "back":  
        print()    
        
def fill():
    print("> fill")
    print()
    global water_amount
    global milk_amount
    global beans_amount
    global cups_count
    global money_amount
    water = int(input("Write how many ml of water do you want to add: "))
    print(">", water)
    milk = int(input("Write how many ml of milk do you want to add: "))
    print(">", milk)
    beans = int(input("Write how many grams of coffee beans do you want to add: "))
    print(">", beans)
    cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    print(">", cups)
    print()
    water_amount += water
    milk_amount += milk
    beans_amount += beans
    cups_count += cups
   
def take():
    global money_amount
    print("> take")
    print()
    print("I gave you $", money_amount)
    money_amount -= money_amount

while True:
    task = input("Write action (buy, fill, take, remaining, exit): ")
    if task == "buy":
        buy()        
    elif task == "fill":
        fill()   
    elif task == "take":
        take()    
    elif task == "remaining":
        remaining()
    elif task == "exit":
        break

print("> exit")    
