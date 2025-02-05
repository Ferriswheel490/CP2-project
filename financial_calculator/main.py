#Fairus tipping calculator


def tipping_calculator():
   
    #ask for bill
    bill = float(input("bill: "))
   
    #ask for tip percentage
    tip_percentage = float(input("tip percentage: "))
    
    #ask if there was more people with you
    more_people = int(input("are there more people: yes/no: "))
    
    #if else for amount of people
    if more_people == "yes":
        num_people = int(input("how many people are there: "))
    else:
        num_people = 1
   
    # Calculate the tip amount
    tip_amount = (tip_percentage / 100) * bill
    
    # Calculate the total bill
    total_bill = bill + tip_amount  
   
    # Calculate the per-person share
    per_person_share = total_bill / num_people