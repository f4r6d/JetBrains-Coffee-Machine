# Write your code here
water = input("Write how many ml of water the coffee machine has: ")
print(">", water)
milk = input("Write how many ml of milk the coffee machine has: ")
print(">", milk)
beans = input("Write how many grams of coffee beans the coffee machine has: ")
print(">", beans)
cups = input("Write how many cups of coffee you will need: ")
print(">", cups)

water_amount = int(water)
milk_amount = int(milk)
beans_amount = int(beans)
cups_needed = int(cups)

max_cups = min(water_amount // 200, milk_amount // 50, beans_amount // 15)
extra_cups = max_cups - cups_needed

if max_cups > cups_needed:
    print("Yes, I can make that amount of coffee (and even", extra_cups, "more than that)")
elif max_cups == cups_needed:
    print("Yes, I can make that amount of coffee")
else:
    print("No, I can make only", max_cups, "cups of coffee")
    
