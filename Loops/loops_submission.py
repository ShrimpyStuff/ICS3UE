#for
#challenge 5
total = 0
for x in range(5):
    while True:
        try:
            num = int(input("Give me a number: "))
            break
        except ValueError:
            print("Not an integer")
    if (input("Should this number be added to the total? (y/n): ").lower() == "y"):
        total += num
print(total)

#challenge 6
while True:
    try: 
        direction =  input("Choose a direction (up/down): ")
        if (direction == "up" or direction == "down"):
            if (direction == ("up")):
                num = int(input("Please supply a number to count to: "))
                for x in range(1, num+1):
                    print(x)
            else:
                while True:
                    num = int(input("Please supply a number under 20: "))
                    if num > 20:
                        print ("Error")
                    else:
                        for x in range(20, num-1, -1):
                            print(x)
                        break
            break
        else:
            print("I don't understand")
    except ValueError:
        print("Not an Integer")

#while
#challenge 3
total = 0;
num0 = int(input("Give me a number to add to the total: "))
total += num0
while True:
    while True:
        try:
            num1 = int(input("Give me another input: "))
            break
        except ValueError:
            print("Not an integer")
    total += num1
    answer = input("Do you want to enter another number (y/n): ").lower()
    if answer != "y":
        break
print(total)

#challenge 5
compnum = 50
attempts = 0
num = 0
while (num != compnum):
    attempts += 1
    while True:
        try:
            num = int(input("Guess a number: "))
            break
        except ValueError:
            print("Not an integer")
    
    if num > compnum:
        print(f"Your guess of {num} is too high")
    elif num < compnum:
        print(f"Your guess of {num} is too low")

print(f"Contrats, you took {attempts} attempts to guess the correct number")

#challenges unit 1
#challenge 4
while True:
    try:
        x = int(input("Supply a starting number: "))
        y = int(input("Supply an ending number: "))
        for i in range(x, y+1):
            print(i)
        break
    except ValueError:
        print("Not of type Integer")

#challenge 6
total = 0;
while True:
    try:
        total = int(input("Supply a number: "))
        while True:
            question = input("Do you want to double the number (y/n): ").lower()
            if question != "y":
                break
            total *= 2
            print(total)
        break
    except ValueError:
        print("Not an integer")