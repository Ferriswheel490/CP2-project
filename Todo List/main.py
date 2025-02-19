#Fairuses code for showing scores and profiles

import sys
import cProfile


def main():
    menu()

def menu():
    
    print("hello welcome to your to do list")
    print("\nHere are your options")
    print()
    
    options = input("""
                    A: make new list
                    B: check lists
                    C: Exit the program
                
                    Please select an option: """)
    if options == "A" or options == "a":
        new_lists()
    elif options == "B" or options == "b":
        ()
    elif options == "C" or options == "c":
        sys.exit
    else:
        print("not an option please choose options from A - D ")
        menu()
def new_lists():
    pass
def check_lists():
    pass



menu()