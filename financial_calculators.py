import math

# Create variables for the different financial calculators

investment = "Investment - To calculate the amount of interest you'll earn on your investment" 
bond = "Bond - To caclulate the amount you'll have to pay on a home loan"

type_1 = "investment"
type_2 = "bond"

 # Using the formatting method ask the user which calculator they want to use
# Error messsage if wrong choice selected

user_calculator = input(f"""{investment}  \n {bond}
                        
    Enter either investment or bond from the menu to proceed:""").lower()
if user_calculator == type_1 or user_calculator == type_2:
    print("Please continue")  
else:
    print("You have selected an invalid option, try again!")

# Variables for two different investment types
# Gather user information with command questions
# Use of simple and compound calculator to work out interest earned
    
simp = "simple"
comp = "compound"

if user_calculator == type_1:
    investment_amount = float(input("Enter the amount you want to deposit:"))
    interest_rate = float(input("What is the interest rate? Enter the number: "))
    num_years = float(input("How many years do you want to invest?: "))
    interest = (input(f"Which type of investment do you want? simple or compound:"))

    if interest == simp:
        simple_interest = investment_amount *(1 + interest_rate/100 * num_years)
        print(f"""The final amount of simple interest after {num_years} years is £ {simple_interest}""")
    
    if interest == comp:
        compound_interest = investment_amount * math.pow((1+ interest_rate/100),num_years)
        print(f"""The final amount of compound interest after {num_years} years is £ {compound_interest}""")

# If user selects bond on the first output screen will ask for user information
# Using bond calculator to work out how much monthly repayments are required
        
elif user_calculator == type_2:
    bond_house_value = float(input("Enter the present value of your house:"))
    bond__interest = float(input("Enter the interest rate: "))
    bond_repay_months = float(input("How many months will you take to repay the bond?:")) 
    monthly_interest = (bond__interest/100)/12
    print (monthly_interest)
    bond_monthly_repayments = (monthly_interest * bond_house_value)/1- (1 +monthly_interest)**(-bond_repay_months)
    print(bond_monthly_repayments)
    print(f"""The final amount of monthy repayments on your house /n over {bond_repay_months} months is £ {bond_monthly_repayments}""")

   