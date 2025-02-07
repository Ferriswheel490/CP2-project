#Fairus test 2 for financial calcilator

# Multi-Functional Financial Calculator
import math


#function for the tippimg calculator
def tip_calculator():
    print("\nTip Calculator")
    
    try:
        bill = float(input("Bill: $ "))
        tip_percentage = float(input("Tip percentage: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    tip_amount = (tip_percentage / 100) * bill
    total_bill = bill + tip_amount

    more_people = input("Were there more people with you? (yes/no): ").strip().lower()
    num_people = 1
    if more_people == "yes":
        try:
            num_people = int(input("How many people were there including you? "))
            if num_people < 1:
                print("Number of people must be at least 1.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    per_person = total_bill / num_people

    print(f"\nTip amount: ${tip_amount:.2f}")
    print(f"Total Bill (including tip): ${total_bill:.2f}")
    print(f"Each person pays: ${per_person:.2f}" if num_people > 1 else f"You pay: ${total_bill:.2f}")


# function saving goal calculator
def savings_goal_calculator():
    print("\nSavings Goal Calculator")

    try:
        goal = float(input("Enter your savings goal: $ "))
        deposit = float(input("Enter your weekly or monthly deposit amount: $ "))
        frequency = input("Will you deposit weekly or monthly? (weekly/monthly): ").strip().lower()
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    if frequency == "weekly":
        time_needed = math.ceil(goal / deposit)
        print(f"It will take approximately {time_needed} weeks to reach your goal.")
    elif frequency == "monthly":
        time_needed = math.ceil(goal / deposit)
        print(f"It will take approximately {time_needed} months to reach your goal.")
    else:
        print("Invalid choice. Please enter 'weekly' or 'monthly'.")


#function for compound intrest
def compound_interest_calculator():
    print("\nCompound Interest Calculator")

    try:
        principal = float(input("Initial deposit: $ "))
        rate = float(input("Annual interest rate (in %): ")) / 100
        years = int(input("Number of years: "))
        times_compounded = int(input("Times interest is compounded per year: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    final_amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    print(f"\nYour savings will grow to: ${final_amount:.2f}")


# function for budget calculator
def budget_allocator():
    print("\nBudget Allocator")

    try:
        income = float(input("Enter your total monthly income: $ "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    categories = {
        "Savings": 0.20,
        "Rent/Mortgage": 0.30,
        "Food": 0.15,
        "Entertainment": 0.10,
        "Utilities": 0.10,
        "Other Expenses": 0.15
    }

    print("\nHere’s how your income should be divided:")
    for category, percentage in categories.items():
        amount = income * percentage
        print(f"{category}: ${amount:.2f}")


# function for sale price calculator
def sale_price_calculator():
    print("\nSale Price Calculator")

    try:
        original_price = float(input("Enter the original price: $ "))
        discount_percentage = float(input("Enter the discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount

    print(f"\nDiscount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")


# The main function that will run every thing
def main():
    print("Welcome to the Financial Toolkit!")
    
    while True:
        print("\nChoose a calculator:")
        print("1. Tip Calculator")
        print("2. Savings Goal Calculator")
        print("3. Compound Interest Calculator")
        print("4. Budget Allocator")
        print("5. Sale Price Calculator")
        print("0. Exit")

        choice = input("\nEnter the number of the calculator you want to use: ").strip()

        if choice == "1":
            tip_calculator()
        elif choice == "2":
            savings_goal_calculator()
        elif choice == "3":
            compound_interest_calculator()
        elif choice == "4":
            budget_allocator()
        elif choice == "5":
            sale_price_calculator()
        elif choice == "0":
            print("Thanks for using the Financial Toolkit! Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
main()
