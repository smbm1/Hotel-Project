#Create a program that asks the user which type of finance option they'd like to calculate.
# If the option selected is investment, ask the user which type of investment they would like, simple or compound interest. 
# ask the user for the number of years they would like to invest over, the deposited amount and the interest rate as an integer, NOT as a percentage.
#if the user selects bond, ask the user for the current value of the house, the annual interest rate as an integer and the number of months they would like to repay the loan over.
import math
def simple_interest(deposit, years, rate):
    interest=rate/100                     # convert to a decimal 
    amount= deposit*(1+interest*years)
    return amount

def compound_interest(deposit,years,rate):
    interest=rate/100
    amount=deposit(1+interest)**years
    return amount

def bond(current_value,interest,months):
    monthly= (interest/100)/12  #divide the decimal by 12 because we are calculating PER MONTH
    amount=(monthly*current_value)/(1-(1+monthly)**-months)
    return amount



while True:
    print("interest: to calculate the amount of interest you'll earn on your investment")
    print("bond: to calculate the amount you'll have to pay on a home loan ")
    type = input("enter 'investment' or 'bond' to proceed: ").lower()
    
    if type not in['investment', 'bond']:
        raise ValueError("Invalid input! Enter 'investment' or 'bond'")
    
    if type=='investment':
        interest_type= input("enter the type of interest : 'simple' or 'compound' ").lower()
        
        if interest_type not in ['simple', 'compound']:
            raise ValueError("INVALID INPUT: Please enter 'simple' or 'compound' ")
        
        deposit = float(input('enter the deposit amount'))
        years = float(input('enter the number of years you wish to invest over '))
        rate =float(input("enter the interest rate as a number ,e.g. 8 percent becomes 8 "))
        
        if interest_type =='simple':
            result = simple_interest(deposit,years,rate)
            print(f"the simple interest is {result-deposit:.2f}")
        
        elif interest_type =='compound':
            result =compound_interest(deposit, years,rate)
            print(f"the compound interest is {result-deposit:.2f}")
        
        
    elif type=='bond':
        current_value =float(input('enter the current value of the house'))
        annual =float(input("enter the annual interest rate as a number e.g 2.5 percent becomes 2.5"))
        months = int(input('enter the number of months you wish to repay the loan over'))
        result = bond(current_value, annual, months)
        
        print(f"The bond value is: {result:.2f}")
        

    
    