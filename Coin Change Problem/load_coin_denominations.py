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