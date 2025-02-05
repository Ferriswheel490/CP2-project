#Fairus test 2 for financial calcilator

def tiping_calculator():
    
    bill = float(input("bill: "))

    tip_percentage =  float(input("tip percentage: "))

    more_people = int(input("was there more people with you: yes/no"))
    if more_people == "yes":
        num_people = int(input("how many people were there with you: "))
        
    else:
        num_people = 1

    

    tip_amount = (tip_percentage/ 100) * bill
