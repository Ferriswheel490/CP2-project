#Fairuses code for showing scores and profiles

import sys
def main():
    menu()

def menu():
    
    print("hello welcome to games'n'stuff")
    print()
    
    options = input("""
                    A: Games
                    B: Scores
                    C: Profiles
                    D: Exsit the program
                
                    Please select an option""")
    if options == "A" or options == "a":
        games()
    elif options == "B" or options == "b":
        scores()
    elif options == "C" or options == "c":
        profiles()
    elif options == "D" or options == "d":
        sys.exit
    else:
        print("not an option please choose options from A - D ")

def games():
    pass
    #Vincent put your games in here

def scores():
    pass

def profiles():
    pass

menu()