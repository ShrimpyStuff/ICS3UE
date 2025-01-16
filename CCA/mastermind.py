import random

colours = ["Blue", "Green", "Red", "Yellow", "Purple", "Orange", "Pink", "Brown"]
loweredColours = [colour.lower() for colour in colours]

def check(bot, userChoices):
    botCopy = bot.copy()
    correctPos = 0
    correctColours = 0
    for i in range(4):
        botIndex = botCopy.index(userChoices[i]) if userChoices[i] in botCopy else -1
        if userChoices[i] == bot[i]:
            correctPos += 1
        elif botIndex != -1:
            if userChoices[botIndex] != userChoices[i]:
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

    while bot != userChoices:
        userChoices = []
        for _ in range(4):
            while True:
                choice = input("Enter a colour: ")
                if choice.lower() in loweredColours:
                    userChoices.append(choice.lower())
                    break
                print("Invalid colour")
        check(bot, userChoices)
        guesses += 1

    print("You won in " + str(guesses) + " guesses")

game()