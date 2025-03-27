# Fairu's coin change problem program
import csv
import os
# Main function
def main():
    print("Welcome to the Coin Changer Program!")
    ans = input("Do you want to enter money to get your change? (yes/no): ").lower()

    if ans == "yes":
        country = input("Select a country (US, Japan, Germany, India): ").strip()

        # Load coins using explicit if-elif conditions
        coins = load_coin_denominations(country)
        if coins is None:
            return

        try:
            amount = int(input("Enter amount (1 - 99): "))
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            return

        result = coin_change(amount, coins)
        if result:
            total_coins, coin_list = result
            print(f"Minimum number of coins needed: {total_coins}")
            for name, count in coin_list:
                print(f"{count} x {name}")

    elif ans == "no":
        print("Goodbye!")
    else:
        print("Invalid response. Please choose 'yes' or 'no'.")
        main()

if __name__ == "__main__":
    main()


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

