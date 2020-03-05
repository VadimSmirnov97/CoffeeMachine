class CoffeeMachine:

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def remainig(self):
        print(
            f'The coffee machine has:\n'
            f'{self.water} of water\n'
            f'{self.milk} of milk\n'
            f'{self.coffee_beans} of coffee beans\n'
            f'{self.cups} of disposable cups\n'
            f'{self.money} of money')

    def buy(self, choised_coffee):
        if choised_coffee == '1':
            if self.water < 250:
                return print('Sorry, not enough water!')
            elif self.coffee_beans < 16:
                return print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                return print('Sorry, not enough cups!')
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            self.money += 4
            return print('I have enough resources, making you a coffee!')
        elif choised_coffee == '2':
            if self.water < 350:
                return print('Sorry, not enough water!')
            elif self.coffee_beans < 20:
                return print('Sorry, not enough coffee beans!')
            elif self.milk < 75:
                return print('Sorry, not enough milk!')
            elif self.cups < 1:
                return print('Sorry, not enough cups!')
            else:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.cups -= 1
                self.money += 7
                return print('I have enough resources, making you a coffee!')
        elif choised_coffee == '3':
            if self.water < 200:
                return print('Sorry, not enough water!')
            elif self.coffee_beans < 12:
                return print('Sorry, not enough coffee beans!')
            elif self.milk < 100:
                return print('Sorry, not enough milk!')
            elif self.cups < 1:
                return print('Sorry, not enough cups!')
            else:
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
                self.cups -= 1
                self.money += 6
                return print('I have enough resources, making you a coffee!')
        else:
            return

    def fill(self, water_fill, milk_fill, coffee_fill, cups_fill):
        self.water += water_fill
        self.milk += milk_fill
        self.coffee_beans += coffee_fill
        self.cups += cups_fill

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


button = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    operation = input('Write action (buy, fill, take, remaining, exit):')
    if operation == 'buy':
        button.buy(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:'))
    elif operation == 'fill':
        button.fill(int(input('Write how many ml of water do you want to add:')),
                    int(input('Write how many ml of milk do you want to add:')),
                    int(input('Write how many grams of coffee beans do you want to add:')),
                    int(input('Write how many disposable cups of coffee do you want to add:')))
    elif operation == 'take':
        button.take()
    elif operation == 'remaining':
        button.remainig()
    elif operation == 'exit':
        break
