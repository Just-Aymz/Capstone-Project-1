import math

"""
REQUEST the user to choose between the investment option and the bond option
STORE the input as user_input 
IF user_input is "Investment"
    REQUEST the user to input the amount of money they are looking to investment    
    STORE the input as a float in the variable principle_amount
    REQUEST the user to input the interest rate 
    STORE the interest rate as a float in the variable interest_rate
    REQUEST the user to input the total investment period
    STORE the variable as investment_period
    REQUEST the user to provide the type of interest they are looking to earn 
    STORE the user inpt as interest_type
    IF interest_type is Simple
        CALCULATE  simple_return = principle_amount * (1 + interest_rate * investment_period)
        STORE the calculation as simple_return
        PRINT "Your return on investment using simple interest is: R{[xxxx.xx]}"
    IF interest_type is Compound
        CALCULATE  compound_return = principle_amount * math.pow((1 + interest_rate), investment_period)
        STORE the calculation as compound_return
        PRINT "Your return on investment using compound interest is: R{[xxxx.xx]}"
IF user_input is "Bond"
    REQUEST the present value of the house from the user
    STORE the input as present_value
    REQUEST the interest rate from the user
    STORE the input as interest_rate    
    REQUEST the length in months they are looking to repay the bond in
    CALCULATE the repayment as repayment = (1 * present_value)/(1 - (1 + interest_rate)**(-n))
    STORE the calculation as bond_repayment
    PRINT "You're repayments per month will be: R{[xxxx.xx]}"
"""

user_input = (
    input(
"""Investment - To calculate the amount of interest you will earn on your.
Bond - To calculate the amount you will have to pay on a home loan.

Enter either 'Investment' or 'Bond' from the menu to proceed: """
).title())

if user_input == 'Investment':
    princple_amount = float(
        input("What is the total rand value of your deposit? ")
        .replace('R','')
    )
    interest_rate = float(
        input("What interest rate will the deposit be growing? ")
        .replace('%','') 
    ) / 100
    investment_period = int(
        input("How long will the investment be earning interest for? ")
    )
    interest_type = input(
        "Will the interest on the deposit be simple or compound? "      
    ).title()
    if interest_type == 'Simple':
        simple_return = round(
            (
            princple_amount * (1 + interest_rate*investment_period)
        ), 2
        )
        print(f"You ROI using simple interest is: R{simple_return}")
    if interest_type == 'Compound':
        compound_return = round(
            (
            princple_amount * math.pow((1 + interest_rate), investment_period)
        ), 2
        )
        print(f"You ROI using simple interest is: R{compound_return}")
elif user_input == 'Bond':
    present_value = float(
        input("What is the current value of the house? ").replace('R','')
    )
    interest_rate = float(
        input("What is the interest rate on the bond? ").replace('%','')
    ) / 100
    repayment_period = int(
        input("What are the number of months you will take to repay the bond: ")
    )
    bond_repayment = round(
        (interest_rate/12) * present_value 
        / (1-((1 + interest_rate/12)**(-repayment_period))), 2
    )
    print(f"You're repayments per month will be: R{bond_repayment}")
else:
    print("You have made an invalid selection")