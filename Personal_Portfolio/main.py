from move_recomender import show
from childs_drawing import childs_drawing
from financial_calculator import money
from personal_library import music
from to_do_list import list
from balancing_equations import ask_to_play

def personal_portfolio():
    while True:
        print("\nWelcome to My Personal Portfolio")
        print("""
        You get to see some of my projects that I made:
          1. Movie Recommender
          2. financial calculator
          3. personal library
          4. Child's Drawing
          5. to do list
          6. balancing equations
          7. Quit
        """)

        try:
            ans = int(input("Which one do you wanna see: "))
        except ValueError:
            print("Please enter a number!")
            continue

        if ans == 1:
            show()
        elif ans == 2:
            money()
        elif ans == 3:
            music()
        elif ans == 4:
            print("Launching Child's Drawing (Coming soon)...")
            # You could launch or link to the Unity game here
        elif ans == 5:
            list()
        elif ans == 6:
            ask_to_play()
        elif ans == 7:
            print("Thanks for visiting! Goodbye!")
            break
        else:
            print("That option isn't ready yet. Stay tuned!")

# Start the portfolio
if __name__ == "__main__":
    personal_portfolio()