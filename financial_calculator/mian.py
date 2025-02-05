#Fairus test 2 for financial calcilator

#function to tip
def tiping_calculator():
    
    #ask the user for the bill
    bill = float(input("bill: $ "))

    #ask the user for the tip percentage
    tip_percentage =  float(input("tip percentage: "))

    #ask the user if there was people with them
    more_people = input("was there more people with you yes/no: ").strip().lower()
    if more_people == "yes":
        num_people = int(input("how many people were there with you: "))
        tip_amount = (tip_percentage/ 100) * bill * num_people
        
    else:
        num_people = 1

    #calculate tip amount
    tip_amount = (tip_percentage/ 100) * bill

    #calculate the total bill
    total_bill =  bill + tip_amount

    #calculate with other people
    per_person = total_bill / num_people

    print(f"\nTip amount: ${tip_amount:.2f}")
    print(f"Total Bill (include tip): ${total_bill:.2f}")
    print(f"Each person pays: ${per_person:.2f}" if num_people > 1 else "You pay: ${total_bill:.2f}")

#where the whol codes runs
tiping_calculator()
