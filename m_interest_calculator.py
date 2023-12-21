"""
#Collect the necessary inputs: principal, apr, years
# calculate the monthly payment
# show to the user
"""

def main(): 
    print("This is a monthly payment laon calculator")

    principal = float(input("Input the loan amount: "))
    apr = input("Input the anual interest rate: ")
    years = int(input("Input the amount of years: "))

    monthly_interest_rate = int(apr)/1200
    number_of_months = years * 12

    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

    print("The monthly payment for this loan is: %.2f" %monthly_payment)

    print("")
while True:
    main()