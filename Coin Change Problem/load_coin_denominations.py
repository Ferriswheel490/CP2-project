import csv

def load_coin_denominations():
    coins = {}
    try:
        with open("Coin Change Problem\\coin_denominations.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                country = row[0].strip()  # Country is in the first column
                coin_name = row[1].strip()  # Coin or note name in the second column
                coin_value = int(row[2].strip())  # Coin or note value in the third column

                # Add coin denominations to the dictionary
                if country not in coins:
                    coins[country] = {}
                coins[country][coin_name] = coin_value
                
        if not coins:
            print("Error: No coin data found.")
            return None
    except FileNotFoundError:
        print("Error: CSV file not found.")
        return None
    return coins
