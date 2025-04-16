
# Function to start the game and ask if the user wants to play
def game():
    print("""
This is a quick text adventure game that I made.
You need to escape the forest in order to survive.
Be careful — your actions have consequences.
I knew about text adventure games and wanted to make one
I learned that this was pretty easy and will do again
""")
    # Ask the user if they want to play and store their response in 'play'
    play = input("Do you wanna play? (y/n): ").lower()

    # If the user answers 'yes' or 'y', start the game
    if play in ("yes", "y"):
        play_game()
    # If the user answers 'no' or 'n', exit the function (game won't start)
    elif play in ("no", "n"):
        return
    # If the user doesn't provide a valid answer, ask again
    else:
        print("Please type yes or no.")

# Function to run the main game logic where the player makes choices
def play_game():
    # Display the introduction text for the game
    print("Welcome to 'Escape the Mysterious Forest'!")
    print("You wake up in a dark forest. The wind howls through the trees.")

    # Ask the player which direction they want to go
    choice1 = input("Do you want to go left or right? (left/right): ").lower()

    # If the player chooses left, present another decision
    if choice1 == "left":
        print("You find a river.")
        # Ask the player if they want to swim or follow the river
        choice2 = input("Do you swim across or follow the river? (swim/follow): ").lower()

        # If the player chooses to swim, they lose the game
        if choice2 == "swim":
            print("You try to swim... but the current is too strong. Game over.")
        # If the player chooses to follow the river, they win the game
        elif choice2 == "follow":
            print("You follow the river and find a road. You're safe! You win!")
        # If the player gives an invalid response, they lose the game
        else:
            print("Invalid choice. Lost in the forest forever.")
    
    # If the player chooses right, present another decision
    elif choice1 == "right":
        print("You run into a bear. Oh no!")
        # Ask the player if they want to climb a tree or play dead
        choice2 = input("Do you climb a tree or play dead? (climb/play): ").lower()

        # If the player chooses to climb, they survive
        if choice2 == "climb":
            print("The bear loses interest and walks away. You survive. You win!")
        # If the player chooses to play dead, they lose the game
        elif choice2 == "play":
            print("The bear is not fooled. Game over.")
        # If the player gives an invalid response, they lose the game
        else:
            print("Invalid choice. The bear eats you. Game over.")
    # If the player makes an invalid choice in the first step, they lose
    else:
        print("You wander aimlessly and never escape. Game over.")

# Function to ask the player if they want to play the game
def ask_to_play():
    # Print a welcome message for the game
    print("\nWelcome to the Text Adventure Game!")
    # Ask the user if they want to play the game and get their response
    ans = input("Do you want to play? (y/n): ").lower()

    # If the player wants to play, start the game
    if ans in ("yes", "y"):
        play_game()
    # If the player doesn't want to play, return to the main menu (or exit)
    else:
        print("Returning to main menu.")
