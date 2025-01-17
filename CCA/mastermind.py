import random

colours = ["Blue", "Green", "Red", "Yellow", "Purple", "Orange", "Pink", "Brown"] #Only used for display purposes
loweredColours = [colour.lower() for colour in colours] # Use lowered colour names when comparing answers

def check(bot, userChoices):
    botCopy = bot.copy() # Make a copy of the array so that you can remove the prechecked values to prevent duplicate counts
    correctPos = 0
    correctColours = 0
    for i in range(4):
        botIndex = botCopy.index(userChoices[i]) if userChoices[i] in botCopy else -1 # Use if and else to check if the index exists cause otherwise an error occurs
        if userChoices[i] == bot[i]:
            correctPos += 1
        elif botIndex != -1: # Check if it is found
            if userChoices[botIndex] != userChoices[i]: #Make sure that there is not a more correct choice
                botCopy[botIndex] = " " # Prevents double counting
                correctColours += 1
    print("\033[92mCorrect colours in correct position: " + str(correctPos) + "\033[0m")
    print("\033[93mCorrect colours in wrong position: " + str(correctColours) + "\033[0m")

def generate():
    return [random.choice(loweredColours) for _ in range(4)] # _ is a throwaway variable as vscode showed a warning

def game():
    bot = generate()
    userChoices = []
    guesses = 0

    print("Enter 4 colours from: " + ", ".join(colours))

    while bot != userChoices: # Wait till the two lists equal each other
        userChoices = []
        for _ in range(4):
            while True:
                choice = input("Enter one colour: ") # Choose one colour at a time
                if choice.lower() in loweredColours:
                    userChoices.append(choice.lower()) # Add choice to user list that will be compared
                    break
                print("Invalid colour")
        check(bot, userChoices)
        guesses += 1

    print("You won in " + str(guesses) + " guesses")

game()