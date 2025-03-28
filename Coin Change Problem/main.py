import csv

# Mapping of currency names to numerical values
CURRENCY_VALUES = {
    "US": {
        "penny": 1, "dime": 10, "quarter": 25, "dollar": 100, "5 dollars": 500
    },
    "Japan": {
        "1 Yen": 1, "5 Yen": 5, "10 Yen": 10, "50 Yen": 50, "100 Yen": 100,
        "500 Yen": 500, "1 Yen bill": 1, "5 Yen bills": 5, "10 Yen bills": 10,
        "50 Yen bills": 50, "100 Yen bills": 100, "1000 Yen Bills": 1000,
        "5000 Yen bills": 5000, "10000 Yen bills": 10000
    },
    "Germany": {
        "1 Euro": 1, "2 Euro": 2, "5 Euro": 5, "10 Euro": 10
    },
    "India": {
        "1 Rupee": 1, "2 Rupee": 2, "5 Rupee": 5, "10 Rupee": 10
    }
}

# Function to load coin denominations from CSV (using predefined values)
def load_coin_denominations():
    coins = {}
    try:
        with open("Coin Change Problem\coin_denominations.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                country = row[0].strip()  # Remove whitespace
                print(f"Loaded country: '{country}'")  # Debugging print

                if country in CURRENCY_VALUES:
                    coins[country] = CURRENCY_VALUES[country]  # Use predefined values
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return None
    return coins


# Function to calculate the minimum coins needed for change
def coin_change(amount, coin_dict):
    coin_values = sorted(coin_dict.values(), reverse=True)  # Sort values from highest to lowest
    coin_names = {v: k for k, v in coin_dict.items()}  # Reverse mapping

    coins_used = []
    total_coins = 0

    for coin in coin_values:
        count = amount // coin
        if count > 0:
            coins_used.append((coin_names[coin], count))
            total_coins += count
            amount -= count * coin

    return total_coins, coins_used

# Main function with input validation and looping
def main():
    coins_data = load_coin_denominations()
    if not coins_data:
        return  # Exit if CSV file is missing

    print("\nWelcome to the Coin Changer Program!")
    
    while True:
        ans = input("\nDo you want to enter money to get your change? (yes/no): ").strip().lower()
        
        if ans == "no":
            print("Goodbye")
            break  # Exit program

        if ans != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue  # Ask again

        while True:
            country = input("\nSelect a country (US, Japan, Germany, India): ").strip()

            if country not in coins_data:
                print("Invalid country. Please choose from the list.")
                continue  # Ask again

            try:
                amount = int(input("\nEnter an amount (1 - 99): "))
                if amount < 1 or amount > 99:
                    print("Error: Please enter an amount between 1 and 99.")
                    continue  # Ask again
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue  # Ask again
            
            # Calculate coin change
            total_coins, coin_list = coin_change(amount, coins_data[country])

            # Display results
            print(f"\nMinimum number of coins needed: {total_coins}")
            for name, count in coin_list:
                print(f"{count} x {name}")
            break  # Go back to the main loop

# Run the program
if __name__ == "__main__":
    main()