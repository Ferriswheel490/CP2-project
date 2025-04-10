from move_recomender import show
from ai_chat_bot import chat
from financial_calculator import money
from personal_library import music
from to_do_list import list

from text_adventure import game  # New import

# my personal portfolio where they are able to pick out things i made
def personal_portfolio():
    while True:
        print("\nWelcome to My Personal Portfolio")
        print("""
        You get to see some of my projects that I made:
          1. Movie Recommender
          2. financial calculator
          3. personal library
          4. ai chat bot
          5. to do list
          6. text adventure
          7. Quit
        """)

        try:
            ans = int(input("Which one do you wanna see: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if ans == 1: #if they choose 1
            show()
        elif ans == 2:#if they choose 2
            money()
        elif ans == 3:#if they choose 3
            music()
        elif ans == 4:#if they choose 4
            chat()
        elif ans == 5:#if they choose 5
            list()
        elif ans == 6:#if they choose 6
            game()
        elif ans == 7:#if they choose 7
            print("Thanks for visiting! Goodbye!")
            break # they leave the progra,
        else:
            print("That option isn't ready yet. Stay tuned!") # handling error

# Start the portfolio
if __name__ == "__main__":
    personal_portfolio()