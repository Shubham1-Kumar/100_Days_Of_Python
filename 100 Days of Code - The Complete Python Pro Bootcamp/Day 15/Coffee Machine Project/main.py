from art import Coffee_cup,Coffee_machine
# created a menu for the coffee machine
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
# resources present in the coffee machine in one go
resources = {
    "water": 500,
    "milk": 500,
    "coffee":300,
}

# price chart
coffee_chart = '''
*------------------------*
| Coffee    | Price in $ |
|************************|                       
| Espresso  | 1.5 $      |
|------------------------|                        
| Latte     | 2.5 $      |
|------------------------|                        
| Cappuccino| 3.0 $      |
*------------------------*
'''
# created a function to check the availability of the resources
def check_resources(choice):
    if resources["water"]>= MENU[choice]["ingredients"]["water"] and resources["milk"]>= MENU[choice]["ingredients"]["milk"] and resources["coffee"]>= MENU[choice]["ingredients"]["coffee"]:
        return True
    else:
        return False

# created a function to verify the transaction
def request_and_receive_money(choice):
    cost = MENU[choice]["cost"]
    money_got = float(input(f"The cost of {choice} is {cost}\nPlease Enter the amount:->"))
    if money_got == cost:
        return True
    else:
        return False

# to make coffee and print report
def make_coffee(coffee_choice):
    remaining_water = resources["water"]-MENU[coffee_choice]["ingredients"]["water"]
    remaining_milk =  resources["milk"]-MENU[coffee_choice]["ingredients"]["milk"]
    remaining_coffee = resources["coffee"]-MENU[coffee_choice]["ingredients"]["coffee"]
    report ={
        "water_left":remaining_water,
        "milk_left":remaining_milk,
        "coffee_left":remaining_coffee
    }
    resources["water"] = remaining_water
    resources["milk"] = remaining_milk
    resources["coffee"]= remaining_coffee
    print("Here is your",coffee_choice)
    Coffee_cup()
    want_report_or_not = input("for report enter 'yes'\nfor not enter 'no'").lower()
    if want_report_or_not == 'yes':
        print(report)
    more_or_not = input("Enter 'yes' for more coffee and 'no' to close.").lower()
    if more_or_not == 'yes':
        coffee_machine()

# coffe machine to do whole process
def coffee_machine():
    # printing the logo of machine
    Coffee_machine()
    # printing the price chart
    print(coffee_chart)
    # initializing a empty var to store user response
    user_choice =""

    # iterating 3 times to avoid any wrong input by also to give them another chance
    i = 3
    while i:
      user_choice = input("What would you like?\nPlease enter the choice from the above chart.\n").lower()
      if user_choice != 'espresso' and user_choice !='latte' and user_choice != 'cappuccino':
          print("Please choose a valid option from the chart")
          i =i-1
      else:
          break
    # checking the available resources for the demand
    if check_resources(user_choice):
        i =3
        while i:
          if request_and_receive_money(user_choice):
            make_coffee(user_choice)
            break
          else:
            print(" Sorry!!!\nWe Can't fulfill your request:")
            print("Insufficient coin entered.\nplease enter enough coin to proceed")
            i=i-1
    else:
        print(" Sorry!!! we run out of resources")
coffee_machine()
