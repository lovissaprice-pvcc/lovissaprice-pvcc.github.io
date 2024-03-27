#Name: Lovissa Price
#Prog purpose: this program computes PVCC tuition and fees based on credits
#   PVCC fee rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
#define tuition and fee rates

RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.5
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.9

#define global variables
inout = 1
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

############### define program functions ##########
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship ammount recieved: "))

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits*RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = RATE_INSTITUTION_FEE * numcredits
    act_fee = RATE_ACTIVITY_FEE * numcredits

    total = tuition + cap_fee + inst_fee + act_fee
    balance = total - scholarship_amt


def display_results():
    currency = '8,.2f'
    line = '--------------------------------------------'

    print(line)
    print('****PIEDMONT VIRGINIA COMM COLLEGE ****')
    print(str(datetime.datetime.now()))
    print(line)
    print('Tuition           $' + format(tuition, currency))
    print('Capital Fee       $' + format(cap_fee, currency))
    print('Institution Fee   $' + format(inst_fee, currency))
    print('Activity Fee      $' + format(act_fee, currency))
    print('Total             $' + format(total, currency))
    print('Balance           $' + format(balance, currency))


#######Call on main program to execute ##########
main()
        
        
