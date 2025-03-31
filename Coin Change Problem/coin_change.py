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
