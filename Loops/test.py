colours = ["\033[31mRed\033[0m", "\033[38:5:202mOrange\033[0m", "\033[33mYellow\033[0m", "\033[32mGreen\033[0m", "\033[34mBlue\033[0m", "\033[38:5:54mIndigo\033[0m","\033[38;2;127;0;255mViolet\033[0m", "\033[36mCyan\033[0m", "\033[35mMagenta\033[0m", "\033[38;2;0;128;102mGeneric viridian\033[0m"]
#RGB ANSI CODES ARE GOATED
while True:
    try:
        start = int(input("What is your starting number between 0 and 4? "))
        end = int(input("What is your end number between 5 and 9? "))
        if (start > 5 or start < 0) or (end < 5 or end > 9):
            print("Not in range")
            continue
        print(", ".join(colours[start:end+1]))#Not inclusive of end so add one
        break
    except ValueError:
        print("Not a valid number")