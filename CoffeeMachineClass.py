# Write your code here
class CoffeeMachine:
    
    water_amount = 400
    milk_amount = 540
    beans_amount = 120
    cups_count = 9
    money_amount = 550

    def remaining(self):
        print("> remaining")
        print()
        print("The coffee machine has:")
        print(self.water_amount, "of water")
        print(self.milk_amount, "of milk")
        print(self.beans_amount, "of coffee beans")
        print(self.cups_count, "of disposable cups")
        print(self.money_amount, "of money")
        print()
    
    def take(self):
        print("> take")
        print()
        print("I gave you $", self.money_amount)
        print()
        self.money_amount -= self.money_amount

    def fill(self):
        print("> fill")
        print()
        water = int(input("Write how many ml of water do you want to add: "))
        print(">", water)
        milk = int(input("Write how many ml of milk do you want to add: "))
        print(">", milk)
        beans = int(input("Write how many grams of coffee beans do you want to add: "))
        print(">", beans)
        cups = int(input("Write how many disposable cups of coffee do you want to add: "))
        print(">", cups)
        print()
        self.water_amount += water
        self.milk_amount += milk
        self.beans_amount += beans
        self.cups_count += cups

    def buy(self):
        print("> buy")
        print()    
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        print(">", coffee_type)
                       
        if coffee_type == "1":
            if self.water_amount < 250:
                print("Sorry, not enough water!")
                print()
            elif self.beans_amount < 16:
                print("Sorry, not enough beans!")
                print()
            elif self.cups_count < 1:
                print("Sorry, not enough cups!")
                print()
            else:
                print("I have enough resources, making you a coffee!")
                print()    
                self.water_amount -= 250
                self.beans_amount -= 16
                self.money_amount += 4
                self.cups_count -= 1
            
        elif coffee_type == "2":
            if self.water_amount < 350:
                print("Sorry, not enough water!")
                print()
            elif self.milk_amount < 75:
                print("Sorry, not enough milk!")
                print()            
            elif self.beans_amount < 20:
                print("Sorry, not enough beans!")
                print()
            elif self.cups_count < 1:
                print("Sorry, not enough cups!")
                print()
            else:
                print("I have enough resources, making you a coffee!")
                print()
                self.water_amount -= 350
                self.milk_amount -= 75
                self.beans_amount -= 20
                self.money_amount += 7
                self.cups_count -= 1
                
        elif coffee_type == "3":
            if self.water_amount < 200:
                print("Sorry, not enough water!")
                print()
            elif self.milk_amount < 100:
                print("Sorry, not enough milk!")
                print()            
            elif self.beans_amount < 12:
                print("Sorry, not enough beans!")
                print()
            elif self.cups_count < 1:
                print("Sorry, not enough cups!")
                print()
            else:
                print("I have enough resources, making you a coffee!")
                print()         
                self.water_amount -= 200
                self.milk_amount -= 100
                self.beans_amount -= 12
                self.money_amount += 6
                self.cups_count -= 1
            
        elif coffee_type == "back":  
            print()    
     
    def choose_action(self, input_string):
        self.input_string = input_string
        if self.input_string == "buy":
            return self.buy()        
        elif self.input_string == "fill":
            return self.fill()   
        elif self.input_string == "take":
            return self.take()    
        elif self.input_string == "remaining":
            return self.remaining()
        elif self.input_string == "exit":
            pass  

my_coffee = CoffeeMachine()     
while True:
  inp = input("Write action (buy, fill, take, remaining, exit): ")
  if inp == "exit":
      print("> exit")
      break
  my_coffee.choose_action(inp)
