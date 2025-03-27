# Fairu's coin change problem program
import csv

# the main function to run the code
def main():
    print("hello and welcome to the coin changer program where you will give me an amount of money and I'll give your respected amount back")
    ans = input("do you wanna put in money to get your change (y/n)\n")
    if ans == "yes" or "y":
        country = input("what country do you want the currency in\n US\n Japan\n Germany\n India\n")
        if country == "US":
            amount = int(input("Enter amount of Dollars 1 - 99: "))
            coin_change_us()
        elif country == "Japan":
            coin_change_japan()
        elif country == "Germany":
            amount = int(input("Enter amount of Euros 1 - 99: "))
            coin_change_inda_germany()
        elif country == "India":
            amount = int(input("Enter amount of Rupees 1 - 99: "))
            coin_change_inda_germany()
    elif ans == "no" or "n":
        print("\ngoodbye")
        exit()
    else:
        print("what is not a respond please choose yes or no")
        return main()
def coin_change_inda_germany():
    pass

def coin_change_japan():
    yen = int(input("Enter amount of Yen 1 - 99: "))
    open("Coin Change Problem\coins.csv")
    

def coin_change_us():
    pass

