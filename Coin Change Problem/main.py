# Fairu's coin change problem program
import csv
import os

# Load coin denominations with if-elif
def load_coin_denominations(country):
    filename = "coin_denominations.csv"
    
    if not os.path.exists(filename):
        print("Error: Coin denomination file not found.")
        return None

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        country_data = {row[0].lower(): [(coin.split('-')[0], int(coin.split('-')[1])) for coin in row[1:]] for row in reader}

    # Using if-elif for explicit country checks
    if country.lower() == "us":
        return country_data.get("us", None)
    elif country.lower() == "japan":
        return country_data.get("japan", None)
    elif country.lower() == "germany":
        return country_data.get("germany", None)
    elif country.lower() == "india":
        return country_data.get("india", None)
    else:
        print(f"Error: No denominations found for {country}.")
        return None

# Coin change calculation using a greedy approach
def coin_change(target, coins):
    if target <= 0:
        print("Error: Amount must be greater than zero.")
        return None

    coins.sort(key=lambda x: x[1], reverse=True)  # Sort coins from largest to smallest
    result = []
    total_coins = 0

    for name, value in coins:
        count = target // value
        if count > 0:
            result.append((name, count))
            total_coins += count
            target -= count * value

    if target > 0:
        print("Error: Cannot make exact change with available denominations.")
        return None

    return total_coins, result

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
