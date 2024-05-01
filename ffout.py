# Name: Lovissa Price
# Prog Purpose: This program creates a payroll report

import datetime

# DEFINE GLOBAL VARIBLES
FED_RATE = 0.12
STATE_RATE = 0.03
SOC_RATE = 0.062
MED_RATE = 0.0145
RET_RATE = 0.04
C = 16.5
S = 15.75
J = 15.75
M = 19.5

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]


num_emps = len(emp)

######### NEW lists for calculated ammounts ########
gross_pay = []
fed_tax = []
state_tax = []
soc_tax = []
med_tax = []
ret_tax = []
total_tax = []
net_pay = []

total_gross = 0
total_net = 0

######### TUPLES of constants #########
#              C    S    J     M
#indexes       0    1    2     3
PAY_RATE = (16.50,15.75,15.75,19.5)

#           fed state soc med   ret
#indexes     0   1     2   3     4
DED_RATE =(0.12,.03,0.062,.0145,.04)

############## define program functions #########
def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
        #calcuate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]

        #calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        soc = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]

        total = -1 * (fed + state + soc + med + ret)
        net = pay - fed - state - soc - med - ret

        # add to totals
        total_gross += pay
        total_net += net

        #append ammounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_tax.append(soc)
        med_tax.append(med)
        ret_tax.append(ret)
        total_tax.append(total)

def create_output_file():
    currency = '8,.2f'
    line ='--------------------------------'
    tab="\t"

############## output file ###############
    out_file = "payroll.txt"
    f = open(out_file, "w")


    f.write(line)
    f.write('\n****** Fresh Foods Market ******')
    f.write('\n---- Weekly Payroll Report -----')
    f.write(tab + str(datetime.datetime.now()))
    f.write(line)
    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "401k" + tab + "Net"
    f.write(titles1 + titles2)

    for i in range(num_emps): 
        dataline1 = emp[i] + " " + job[i] + " " + format(gross_pay[i], currency) + tab + format(fed_tax[i], currency) + tab + format(state_tax[i], currency) + tab + format(soc_tax[i], currency) + " " + format(med_tax[i], currency) + "  " + format(ret_tax[i], currency) + " " 
        dataline2 = format(total_tax[i], currency)
        f.write(dataline1 + dataline2)

    f.write(line)
    f.write("**************** TOTAL GROSS: $" + format(total_gross, currency))
    f.write("**************** TOTAL NET  : $" + format(total_net, currency))
    f.close()
    print("Open " + out_file + " to view your report")


####### call on main #####
main()
        
        
        


    
    
    

