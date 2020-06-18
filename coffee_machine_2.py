# Write your code here
water_amount = 400
milk_amount = 540
beans_amount = 120
cups_count = 9
money_amount = 550

def print_supplies():
    print("The coffee machine has:")
    print(water_amount, "of water")
    print(milk_amount, "of milk")
    print(beans_amount, "of coffee beans")
    print(cups_count, "of disposable cups")
    print(money_amount, "of money")

print_supplies()
print()
option_picker = input("Write action (buy, fill, take): ")
print(">", option_picker)

def buy():
    global water_amount
    global milk_amount
    global beans_amount
    global cups_count
    global money_amount
    coffee_type = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    print(">", coffee_type)
    if coffee_type == 1:
        water_amount -= 250
        beans_amount -= 16
        money_amount += 4
        cups_count -= 1
    elif coffee_type == 2:
        water_amount -= 350
        milk_amount -= 75
        beans_amount -= 20
        money_amount += 7
        cups_count -= 1
    elif coffee_type == 3:
        water_amount -= 200
        milk_amount -= 100
        beans_amount -= 12
        money_amount += 6
        cups_count -= 1

def fill():
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
    water_amount += water
    milk_amount += milk
    beans_amount += beans
    cups_count += cups

if option_picker == "buy":
    buy()
elif option_picker == "fill":
    fill()
elif option_picker == "take":
    print("I gave you $", money_amount)
    money_amount -= money_amount

print()    
print_supplies()
        
