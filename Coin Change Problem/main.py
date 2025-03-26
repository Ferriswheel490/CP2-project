# Fairu's coin change problem program
import sys
# the main function
def main():
    print("hello and welcome to the coin changer program where you will give me an amount of money and I'll give your respected amount back")
    ans = input("do you wanna put in money to get your change (y/n): ")
    if ans == "yes":
        country = input("what country do you want the currency in\n US\n Japan\n Germany\n India: ")
        if country == "US":
            amount = int(input("Enter amount of Dollars 1 - 99: "))
            coin_change_us()
        elif country == "Japan":
            amount = int(input("Enter amount of Yen 1 - 99: "))
            coin_change_japan()
        elif amount == "Germany":
            money = int(input("Enter amount of Euros 1 - 99: "))
            coin_change_inda_germany()
        elif amount == "India":
            money = int(input("Enter amount of Rupees 1 - 99: "))
            coin_change_inda_germany()
    elif ans == "no":
        sys.exit()
    else:
        print("what is not a respond please choose yes or no")
        return main()

def coin_change_inda_germany():
    pass

def coin_change_japan():
    pass

def coin_change_us():
    pass