# Fairus Test 2 – Multi-Functional Financial Toolkit

import math  # Import math module to use mathematical functions like ceil() for rounding up

# Entry point for the portfolio and calling the main function for the financial toolkit
def money():
    print("""
Welcome to my Financial Calculator!

This tool helps you with:
- Tip calculation
- Saving goal estimation
- Compound interest calculation
- Budget allocation
- Sale price discounts
this was one of my fist things to make in class
I learned many more things in python when doing this
    """)

    # Ask if the user wants to use the financial toolkit
    ans = input("Do you want to use it? (y/n): ").strip().lower()
    if ans in ("yes", "y"):  # If the user agrees, run the calculator function
        calculate()
    elif ans in ("no", "n"):  # If the user declines, exit the function
        return
    else:
        # If input is invalid, print a message and return to the portfolio
        print("Not a valid option. Returning to portfolio.")

# Tip Calculator - calculates tip amount based on the bill and tip percentage
def tip_calculator():
    print("\nTip Calculator")
    
    try:
        # Prompt user for bill amount and tip percentage
        bill = float(input("Bill: $ "))
        tip_percentage = float(input("Tip percentage: "))
    except ValueError:
        # Handle invalid input for non-numeric values
        print("Invalid input. Please enter numbers only.")
        return

    # Calculate the tip amount and total bill
    tip_amount = (tip_percentage / 100) * bill
    total_bill = bill + tip_amount

    # Ask if there are other people and calculate the cost per person
    more_people = input("Were there more people with you? (yes/no): ").strip().lower()
    num_people = 1
    if more_people == "yes":
        try:
            # Get the number of people and calculate each person's share
            num_people = int(input("How many people including you? "))
            if num_people < 1:
                print("Number of people must be at least 1.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    # Calculate how much each person has to pay
    per_person = total_bill / num_people
    print(f"\nTip: ${tip_amount:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    print(f"Each pays: ${per_person:.2f}" if num_people > 1 else f"You pay: ${total_bill:.2f}")

# Savings Goal Calculator - helps user estimate how long it will take to save a certain amount
def savings_goal_calculator():
    print("\nSavings Goal Calculator")

    try:
        # Prompt user for their savings goal and deposit details
        goal = float(input("Your savings goal: $ "))
        deposit = float(input("Weekly or monthly deposit amount: $ "))
        frequency = input("Will you deposit weekly or monthly? (weekly/monthly): ").strip().lower()
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Calculate the time needed to reach the savings goal
    if frequency == "weekly":
        time_needed = math.ceil(goal / deposit)  # Use math.ceil to round up the result
        print(f"It will take approximately {time_needed} weeks to reach your goal.")
    elif frequency == "monthly":
        time_needed = math.ceil(goal / deposit)
        print(f"It will take approximately {time_needed} months to reach your goal.")
    else:
        print("Invalid choice. Please enter 'weekly' or 'monthly'.")

# Compound Interest Calculator - calculates the compound interest on an investment
def compound_interest_calculator():
    print("\nCompound Interest Calculator")

    try:
        # Prompt user for the initial deposit, interest rate, and number of years
        principal = float(input("Initial deposit: $ "))
        rate = float(input("Annual interest rate (in %): ")) / 100  # Convert percentage to decimal
        years = int(input("Number of years: "))
        times_compounded = int(input("Times compounded per year: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Calculate the final amount after applying compound interest
    final_amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    print(f"\nYour savings will grow to: ${final_amount:.2f}")

# Budget Allocator - suggests a budget breakdown based on the user's monthly income
def budget_allocator():
    print("\nBudget Allocator")

    try:
        # Prompt user for their total monthly income
        income = float(input("Your total monthly income: $ "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Dictionary for budget categories and the percentage of income to allocate
    categories = {
        "Savings": 0.20,
        "Rent/Mortgage": 0.30,
        "Food": 0.15,
        "Entertainment": 0.10,
        "Utilities": 0.10,
        "Other Expenses": 0.15
    }

    # Calculate and display the recommended budget breakdown
    print("\nRecommended Budget Breakdown:")
    for category, percentage in categories.items():
        amount = income * percentage
        print(f"{category}: ${amount:.2f}")

# Sale Price Calculator - calculates the discounted price based on original price and discount percentage
def sale_price_calculator():
    print("\nSale Price Calculator")

    try:
        # Prompt user for original price and discount percentage
        original_price = float(input("Original price: $ "))
        discount_percentage = float(input("Discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    # Calculate the discount amount and final price after discount
    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount

    print(f"\nDiscount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")

# Main loop for the calculator menu, where the user can select an option
def calculate():
    print("Welcome to the Financial Toolkit!")
    
    while True:
        # Display the available options for the user
        print("""
Choose a calculator:
1. Tip Calculator
2. Savings Goal Calculator
3. Compound Interest Calculator
4. Budget Allocator
5. Sale Price Calculator
0. Exit
""")
        # Get the user's choice
        choice = input("Enter your choice: ").strip()

        # Call the appropriate function based on the user's choice
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
            # Exit the program
            print("Thanks for using the Financial Toolkit! Returning to portfolio...")
            break
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

# Only runs when this file is executed directly, not when imported
if __name__ == "__main__":
    money()
