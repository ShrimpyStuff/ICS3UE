import random
import time

ainame = random.choice(["David", "Ian", "Matthew", "Luke", "Mark", "Saul", "Leviticus", "Samuel"])

board = ["-"]*24
score = 0
winStreak = 0
name = ""

def clear(lines: int = 1):
    for x in range(lines):
            print("\033[K", end="", flush=True)
            print("\033[A", end="", flush=True)
            print("\033[K", end="", flush=True)

def draw():
    clear(1)
    print("\033[32m" + " ".join(board) + "\033[0m")

def player_turn(rangeNum):
    global board
    while True:
        try:
            turnLen = int(input("Choose a number between 1 and 3: "))
            if turnLen > 0 and turnLen <= 3:
                newNum = rangeNum-turnLen
                if newNum < 0: newNum = 0
                board[newNum:rangeNum] = ["X"]*turnLen
                clear(1)
                return newNum
            else:
                print("Must be between 1 and 3")
                time.sleep(0.5)
                clear(2)
        except ValueError:
            print("Not an integer")
            time.sleep(0.5)
            clear(2)

def bot_turn(rangeNum):
    global board
    turnLen = random.randint(1,3)
    newNum = rangeNum-turnLen
    if newNum < 0: newNum = 0
    board[newNum:rangeNum] = ["O"]*turnLen
    return newNum

def game():
    global name, score, board, winStreak
    board = ["-"]*24
    lastNum = len(board)
    turn = bool(random.getrandbits(1)) #Apparently considerably faster than randInt. Makes sense

    print("Hello, " + name + ", " + "my name is", ainame)
    print("This game is called the subtraction game")
    print("The goal of this game is to remove either 1, 2, or 3, sticks in your turn and not be the player to take the last stick")
    print("The game will randomly choose who starts between you and " + ainame)

    print("You start" if turn else "Bot starts")
    time.sleep(1)
    clear(1)
    print(" ".join(board))
    while (board[0] == "-"):
        if turn:
            lastNum = player_turn(lastNum)
        else: lastNum = bot_turn(lastNum)
        turn = not turn
        draw()
    print("Winner is " + (ainame if (board[0] == "X") else name))
    if board[0] == "O":
        winStreak += 1
        score += 1
    else: winStreak = 0

while True:
    choice = input("A) Play Game. B) See Results. C) Exit. ").lower()

    if choice == "play game" or choice == "a":
        print("Hello. Welcome")
        name = input("What is your name? ")
        game()
    elif choice == "see results" or  choice == "b":
        print(f"You have won {score} total games! You're winstreak is {winStreak}")
    elif choice == "exit" or  choice == "c":
        break
    elif choice != "exit":
        print("Not a valid option")
        continue