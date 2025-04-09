# financial_calculator.py
# Fairus Test 2 – Multi-Functional Financial Toolkit

import math

# Entry point for your portfolio
def money():
    print("""
Welcome to my Financial Calculator!

This tool helps you with:
- Tip calculation
- Saving goal estimation
- Compound interest calculation
- Budget allocation
- Sale price discounts
    """)

    ans = input("Do you want to use it? (y/n): ").strip().lower()
    if ans in ("yes", "y"):
        calculate()
    elif ans in ("no", "n"):
        return
    else:
        print("Not a valid option. Returning to portfolio.")

# Tip Calculator
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
            num_people = int(input("How many people including you? "))
            if num_people < 1:
                print("Number of people must be at least 1.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    per_person = total_bill / num_people
    print(f"\nTip: ${tip_amount:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    print(f"Each pays: ${per_person:.2f}" if num_people > 1 else f"You pay: ${total_bill:.2f}")

# Savings Goal Calculator
def savings_goal_calculator():
    print("\nSavings Goal Calculator")

    try:
        goal = float(input("Your savings goal: $ "))
        deposit = float(input("Weekly or monthly deposit amount: $ "))
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

# Compound Interest Calculator
def compound_interest_calculator():
    print("\nCompound Interest Calculator")

    try:
        principal = float(input("Initial deposit: $ "))
        rate = float(input("Annual interest rate (in %): ")) / 100
        years = int(input("Number of years: "))
        times_compounded = int(input("Times compounded per year: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    final_amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    print(f"\nYour savings will grow to: ${final_amount:.2f}")

# Budget Allocator
def budget_allocator():
    print("\nBudget Allocator")

    try:
        income = float(input("Your total monthly income: $ "))
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

    print("\nRecommended Budget Breakdown:")
    for category, percentage in categories.items():
        amount = income * percentage
        print(f"{category}: ${amount:.2f}")

# Sale Price Calculator
def sale_price_calculator():
    print("\nSale Price Calculator")

    try:
        original_price = float(input("Original price: $ "))
        discount_percentage = float(input("Discount percentage: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    discount_amount = (discount_percentage / 100) * original_price
    final_price = original_price - discount_amount

    print(f"\nDiscount Amount: ${discount_amount:.2f}")
    print(f"Final Price: ${final_price:.2f}")

# Main loop for the calculator menu
def calculate():
    print("Welcome to the Financial Toolkit!")
    
    while True:
        print("""
Choose a calculator:
1. Tip Calculator
2. Savings Goal Calculator
3. Compound Interest Calculator
4. Budget Allocator
5. Sale Price Calculator
0. Exit
""")
        choice = input("Enter your choice: ").strip()

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
            print("Thanks for using the Financial Toolkit! Returning to portfolio...")
            break
        else:
            print("Invalid choice. Please try again.")

# Only runs when this file is run directly
if __name__ == "__main__":
    money()
