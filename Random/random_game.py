import random


def game():
    names = [""]
    name = random.choice(names)
    print("Hello my name is ", name)
    print("This game is called ")

while True:
    choice = input("Play Game. See Results. Exit. ").lower()

    if choice == "play game":
        print("Hello. Welcome")
        game()
    elif choice == "see results":
        print("You have a high score of: , Past Results: ")
    elif choice != "exit":
        print("Not a valid option")
        continue
    break