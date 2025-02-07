#Fairus test 2 for financial calcilator

# Function to calculate tip
def tiping_calculator():
    
    # Ask the user for the bill amount
    try:
        bill = float(input("Bill: $ "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the bill.")
        return
    
    # Ask the user for the tip percentage
    try:
        tip_percentage = float(input("Tip percentage: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the tip percentage.")
        return

    # Calculate the tip amount
    tip_amount = (tip_percentage / 100) * bill

    # Calculate the total bill including the tip
    total_bill = bill + tip_amount

    # Ask the user if they were with more people
    more_people = input("Were there more people with you? (yes/no): ").strip().lower()

    if more_people == "yes":
        try:
            num_people = int(input("How many people were there including you? "))
            if num_people < 1:
                print("Number of people must be at least 1.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number of people.")
            return
    else:
        num_people = 1

    # Calculate per-person cost
    per_person = total_bill / num_people

    # Display results
    print(f"\nTip amount: ${tip_amount:.2f}")
    print(f"Total Bill (including tip): ${total_bill:.2f}")
    
    if num_people > 1:
        print(f"Each person pays: ${per_person:.2f}")
    else:
        print(f"You pay: ${total_bill:.2f}")

# Run the function
tiping_calculator()
