#NAME: Lovissa Price
#PROG PURPOSE: this program finds the price of a meal at Palermo Pizza

import datetime

############# define global variables ###############
PRICE_SMALL = 9.99
PRICE_MED = 12.99
PRICE_LARGE = 17.99
PRICE_XLARGE = 21.99
PRICE_DRINK = 3.99
PRICE_BREAD = 6.99
SALES_TAX_RATE = 0.055

#define globals vars
num_pizzas = 0
num_drinks = 0
num_bread = 0
cost_pizza = 0
cost_drinks = 0
cost_bread = 0
subtotal = 0
sales_tax = 0
total = 0

############ define program functions #############
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order again? (Y/N)")
        if yesno.upper() == "N":
            more = False
            print("Thank you for your order! Enjoy your pizza!")

def get_user_data():
    global pizza_size, num_pizzas, num_drinks, num_bread
    print('**********Palermo Pizza***********')
    print('S small pizza               $ 9.99')
    print('M medium pizza              $12.99')
    print('L large pizza               $17.99')
    print('X extra large pizza         $21.99')
    print('Drinks                      $3.99')
    print('Breadsticks                 $6.99')

    pizza_size = input("\nWhat size pizza would you like to order? (S, M, L, X): ")
    pizza_size = pizza_size.upper()

    num_pizzas = int(input("Number of pizzas: "))
    num_drinks = int(input("Number of drinks: "))
    num_bread = int(input("Number of breadstick orders: "))

def perform_calculations():
    global cost_pizza, cost_drinks, cost_bread, subtotal, sales_tax, total

    if pizza_size == "S" or pizza_size == "s":
        cost_pizza = num_pizzas * PRICE_SMALL
    elif pizza_size == "M" or pizza_size == "m":
        cost_pizza = num_pizzas * PRICE_MED
    elif pizza_size == "L" or pizza_size == "l":
        cost_pizza = num_pizzas * PRICE_LARGE
    else:
        cost_pizza = num_pizzas * PRICE_XLARGE

    cost_drinks = num_drinks * PRICE_DRINK
    cost_bread = num_bread * PRICE_BREAD

    subtotal = cost_pizza + cost_drinks + cost_bread
    sales_tax = subtotal * SALES_TAX_RATE
    total = sales_tax + subtotal

def display_results():
    currency = '8,.2f'
    line = '----------------------------'
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]

    print(line)
    print('********Palermo Pizza*******')
    print(short_date)
    print(line)
    print('Number of pizzas ordered: '+ str(num_pizzas))
    print(line)
    print('Pizzas          $' + format(cost_pizza,currency))
    print('Drinks          $' + format(cost_drinks,currency))
    print('Breadsticks     $' + format(cost_bread,currency))
    print('Subtotal        $' + format(subtotal,currency))
    print('Sales Tax       $' + format(sales_tax,currency))
    print('Total           $' + format(total,currency))

#########call on main program to execute###########
main()
    
            
    
