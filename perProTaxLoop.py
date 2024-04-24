#NAME: Lovissa Price

import datetime

######## define global variables ###########
ANNUAL_TAX_RATE = 0.042



#Define global variables
car_value = 0
annual_ammount = 0
tax_due = 0
total_due = 0
relief_amt = 0



def main():
    own_car = True

    while own_car:  
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to fill out the form again?(Y/N)")
        if yesno.upper() == "N":
                own_car = False
                print("Thank you for completing this form!")
                
        

def get_user_data():
    global car_value, tax_due
    car_value = int(input("Please enter the assesed value of your vehicle: "))
    yesno = input("\nIs your car predominately used for non-business purposes & uses passenger license plates?(Y/N)")
    if yesno == "Y" or yesno == "y":
        tax_due = (car_value * ANNUAL_TAX_RATE) * 0.67
    else:
        tax_due = car_value * ANNUAL_TAX_RATE
    
          
    
def perform_calculations():
    global tax_due, total_due, relief_amt
    total_due = (tax_due) / 2
    relief_amt = ((car_value * ANNUAL_TAX_RATE)/2)*0.33


def display_results():
    currency='8,.2f'
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]


    
    print('-----------------------------------------------------------')
    print('** Personal Property Tax for Vehicles in Charlottesville **')
    print('----------------------------------------------------------')
    print(short_date)
    print('-----------------------------------------------------------')
    print('Assesed car value:      $' + format(car_value, currency))
    print('Relief ammount:         $' + format(relief_amt, currency))
    print('Annual ammount owed:    $' + format(tax_due, currency))
    print('Total due:              $' + format(total_due, currency))

main()
    
    

    
    
    
    
