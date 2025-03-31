import load_coin_denominations
import coin_change

# Main function with input validation and looping
def main():
    coins_data = load_coin_denominations.load_coin_denominations()  # Call the function correctly
    if not coins_data:
        return  # Exit if CSV file is missing or empty

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
            total_coins, coin_list = coin_change.coin_change(amount, coins_data[country])

            # Display results
            print(f"\nMinimum number of coins needed: {total_coins}")
            for name, count in coin_list:
                print(f"{count} x {name}")
            break  # Go back to the main loop

# Run the program
if __name__ == "__main__":
    main()
