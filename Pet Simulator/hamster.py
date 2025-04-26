import random
import time

is_hamster_alive = True
hamster_status = {
    "hunger": 100,
    "happiness": 100,
    "cleanliness": 100,
    "age": 0,
    "dead": False,
}

def show_hamster_intro():
    print(r"""
                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀
                                                    ⡠⠀⢄⡀⠀⣀⠀⠀⢀⣀⡴⠉⠀⠃⠀⠀⠀⠀⠀⠀
                                                    ⢇⠀⠀⣿⣾⣯⣍⣽⣿⣿⣿⡤⢀⠇⠀⠀⠀⠀⠀⠀
                                                    ⠀⠑⢼⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣤⡀⠀⠀⠀⠀⠀
                                                    ⠀⢸⣿⣿⣟⣻⣿⣿⣿⣭⣿⣿⣿⣿⡟⠢⡀⠀⠀⠀
                                                    ⠀⢸⡏⢻⣿⢿⣿⣿⣿⡿⣿⡟⣿⠟⠀⠀⣿⣦⠀⠀
                                                    ⠀⢸⠛⠮⠝⢋⠙⣻⣊⢁⠈⠚⢃⣀⣴⣾⣿⣿⣷⡀
                                                    ⠀⣾⣶⣤⡠⠀⠉⠀⠈⢀⢀⣾⣿⣿⣿⣿⣿⣿⠿⣧
                                                    ⠀⠿⡟⠛⠻⠷⣶⠀⣶⠟⠋⠛⣿⠗⠈⠈⠉⢠⣪⣿
                                                    ⠀⠸⡈⠙⣄⡀⢸⢸⡿⣄⡦⠋⠁⠀⠀⠀⡠⣺⣿⣿
                                                    ⠀⠀⠙⢢⡤⠙⠛⡏⣅⣠⠶⠖⠒⠒⠈⠁⠐⢾⣿⡏
                                                    ⠀⠀⠀⠈⡄⠀⠀⠸⣿⡷⠀⠀⠀⠀⠀⢀⢠⣿⣿⠃
                                                    ⠀⠀⠀⠀⠘⠦⣀⠀⣿⣷⣦⠄⠀⠀⠀⢝⣿⣿⡟⠀
                                                    ⠀⠀⠀⣤⣤⣄⣊⡉⠟⠿⢿⡷⠗⠚⣲⠽⠿⠟⠁⠀
    """)
    print("This is your hamster. Take good care of it.")

    if random.randint(1, 100) == 1:
        show_monstrosity()

def show_monstrosity():
    print(r"""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⠒⠒⠒⠒⠒⠒⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣶⣶⡄⠀⠀⠀⠀⠀⠀⠈⢻⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡋⣄⣀⠸⣿⣀⠀⠀⠀⠀⢠⣴⠟⠋⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⠈⠁⠀⠀⠀⠀⠈⠁⣠⣾⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣷⣿⣹⠏⠀⠀⠀⠀⠀⠀⠀⠘⠋⢻⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡤⠞⠋⢸⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⡇⠘⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠉⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠚⡟⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣵⣀⣀⣀⣯⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠸⠶⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠾⠿⡹⠋⠻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⡀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⢖⠪⠭⢿⣦⣤⠿⠟⣛⠶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠈⠟⠲⠶⠶⣦⣶⣦⣬⣁⣭⣶⠿⢿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢦⡀⠀⠒⢷⣶⣄⣌⣑⣻⣟⠉⢡⣴⠟⠁⠀⠀⢀⣤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡇⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠁⠀⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀
                                ⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀
                                ⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡆⠀⠀
                                ⠀⠠⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠤⢤⣀⣀⣠⠤⠤⠤⠴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀
                                ⠀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀
                                ⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣠
                                ⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠰⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡛⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
                                ⠆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢷⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
                                ⠀⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇
        """)
    print("CONGRATS! You somehow got this monstrosity of a hamster. It stares into your soul.")

def name_hamster():
    name = input("What do you want to name your hamster? ")
    print(f"So the name is: {name}")
    accept = input("Do you like the name? (yes/no): ").lower()

    if accept == "yes":
        print(f"Great! {name} is now your pet hamster.")
        return name
    else:
        print("Alright, let's try again.")
        return name_hamster()

def care_loop():
    show_hamster_intro()
    hamster_name = name_hamster()

    while True:
        if hamster_status["dead"]:
            print("\n💀 Your hamster has died. Game over.")
            break

        print(f"\nWhat would you like to do with {hamster_name}?")
        print("1. Feed")
        print("2. Play")
        print("3. Clean")
        print("4. AFK (Do nothing and let time pass)")
        print("5. Check Status")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            hamster_status["hunger"] = min(hamster_status["hunger"] + 10, 100)
            print(f"{hamster_name} enjoyed the food! 🍎")
        elif choice == "2":
            hamster_status["happiness"] = min(hamster_status["happiness"] + 10, 100)
            print(f"{hamster_name} had fun playing! 🧸")
        elif choice == "3":
            hamster_status["cleanliness"] = min(hamster_status["cleanliness"] + 10, 100)
            print(f"{hamster_name} is clean and happy! 🛁")
        elif choice == "4":
            print(f"{hamster_name} is left alone...")
            afk_event(hamster_name)
        elif choice == "5":
            print_status(hamster_name)
        elif choice == "6":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

        # Update hamster stats and check if dead after each action
        update_stats()

        time.sleep(1)


def update_stats():
    hamster_status["age"] += 1
    hamster_status["hunger"] -= 5
    hamster_status["happiness"] -= 5
    hamster_status["cleanliness"] -= 5

    if hamster_status["hunger"] <= 0 or hamster_status["happiness"] <= 0 or hamster_status["cleanliness"] <= 0:
        hamster_status["dead"] = True
        print("\n💀 Your hamster has died due to neglect. You can no longer take care of it.")
        
def afk_event(name):
    event = random.randint(1, 4)

    if event == 1:
        print(f"{name} just took a nap. Nothing happened.")
    elif event == 2:
        print(f"{name} chewed on a paper towel. It was fun.")
    elif event == 3:
        print(f"{name} got startled by a loud noise.")
    elif event == 4:
        print(f"💀 Tragedy! {name} escaped and fell behind the dresser.")
        hamster_status["dead"] = True

def print_status(name):
    print("\n🐹 Hamster Status:")
    if hamster_status["dead"]:
        print(f"{name} is DEAD 💀")
    else:
        print(f"Hunger: {hamster_status['hunger']}")
        print(f"Happiness: {hamster_status['happiness']}")
        print(f"Cleanliness: {hamster_status['cleanliness']}")
        print(f"Age: {hamster_status['age']}")
        print(f"Dead: {hamster_status['dead']}")
        print(f"Name: {name}")
        print(f"Status: {'Alive' if not hamster_status['dead'] else 'Dead'}")