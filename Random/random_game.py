import random
import time

ainame = random.choice(["Sajid", "David", "Ian", "Matthew", "Luke", "Mark", "Saul", "Leviticus", "Samuel"])

name = ""

def game():
    global name
    print("Hello, " + name + ", " + "my name is", ainame)
    print("This game is called ")

while True:
    choice = input("Play Game. See Results. Exit. ").lower()

    if choice == "play game":
        print("Hello. Welcome")
        name = input("What is your name? ")
        game()
    elif choice == "see results":
        print("You have a high score of: , Past Results: ")
    elif choice != "exit":
        print("Not a valid option")
        continue
    break

print('\033[?25h', end="") #'\033[?25h to show \033[?25l to hide'

def clear(lines: int = 1):
    for x in range(lines):
            print("\033[K", end="", flush=True)
            print("\033[A", end="", flush=True)
            print("\033[K", end="", flush=True)