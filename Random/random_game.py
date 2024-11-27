import random

while True:
    choice = input("Play Game. See Results. Exit. ").lower()

    if choice == "play game":
        print("Hello. Welcome")
    elif choice == "see results":
        print("You have a high score of: , Past Results: ")
    elif choice != "exit":
        print("Not a valid option")
        continue
    break
