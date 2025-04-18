from create_pet import create_pet
from hamster import hamster

def main():
    print("""
Welcome to the pet simluator
Here you can create a pet and name it
Take care of your pet and watch it grow up
""")
    ans = input("do you wanna create a pet (y/n): ")
    if ans == "yes" or "y":
        create_pet()
    if ans == "no" or "n":
        print("ok bye")
    else:
        print("bye then")

main()