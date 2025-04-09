import tkinter as tk
from random import choice
import sys
import tkinter.messagebox as messagebox

# Sample equations (can be expanded)
equations = [
    ('H2 + O2 -> H2O', '2H2 + O2 -> 2H2O'),
    ('Na + Cl2 -> NaCl', '2Na + Cl2 -> 2NaCl'),
    ('C + O2 -> CO2', 'C + O2 -> CO2'),
]

# Global variables to track attempts and the correct answer
attempts = 0
max_attempts = 3
correct_answer = ''
correct_example = ''

# Function to check if the equation is balanced
def check_answer():
    global attempts
    user_input = equation_entry.get()
    attempts += 1

    if user_input == correct_answer:
        result_label.config(text="Correct!", fg="green")
        reset_game()  # Move to next question after a correct answer
    elif attempts < max_attempts:
        result_label.config(text=f"Incorrect! Try again. Attempts left: {max_attempts - attempts}", fg="red")
        if attempts == 2:  # On second try, show example
            show_example()
    else:
        result_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")
        show_example()
        reset_game()  # Reset after 3 attempts

# Show example if the answer is incorrect
def show_example():
    example_label.config(text="Example: " + correct_example)

# Generate a random equation to balance
def generate_equation():
    global correct_answer, correct_example, attempts
    equation, answer = choice(equations)
    equation_label.config(text="Balance this equation: " + equation)
    correct_answer = answer
    correct_example = "To balance this: Add coefficients like '2' in front of atoms."
    attempts = 0  # Reset attempts when a new equation is generated
    result_label.config(text="")
    example_label.config(text="")

# Reset game after a correct answer or after 3 attempts
def reset_game():
    generate_equation()

# Function to exit and return to main menu
def exit_game(event=None):
    root.quit()
    sys.exit()

# Function to ask if the user wants to play
def ask_to_play():
    response = messagebox.askyesno("Play?", "Do you want to play the balancing equations game?")
    if response:
        start_game()
    else:
        root.quit()  # Exit if they don't want to play

# Function to start the game
def start_game():
    # Setting up the GUI
    global root, equation_label, equation_entry, result_label, example_label
    root = tk.Tk()
    root.title("Balance Chemical Equations")

    # Labels, Entry, and Buttons
    equation_label = tk.Label(root, text="Balance this equation: ", font=("Arial", 14))
    equation_label.pack()

    equation_entry = tk.Entry(root, font=("Arial", 14))
    equation_entry.pack()

    submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=check_answer)
    submit_button.pack()

    result_label = tk.Label(root, text="", font=("Arial", 14))
    result_label.pack()

    example_label = tk.Label(root, text="", font=("Arial", 12))
    example_label.pack()

    # Generate a new equation when the program starts
    generate_equation()

    # Bind Escape key to exit and return to main menu
    root.bind("<Escape>", exit_game)

    root.mainloop()

# Start the program by asking the user if they want to play
ask_to_play()
