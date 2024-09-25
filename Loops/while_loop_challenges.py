# challenge 1
total = 0
while (total <=50):
    try:
        num = int(input("Input a number to add to the total: "))
        total += num
        print(f"The total is {total}")
    except ValueError:
        print("Not an integer")

#challenge 2
while True:
    try:
        num = int(input("Give me a number: "))
        if num > 5:
            break
    except ValueError:
        print("Not an Integer")

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

#challenge 4
total = 0;
while True:
    name = input("Enter a name for the guest list: ")
    total += 1
    question = input("Do you want to invite another guest (y/n): ").lower()
    if question != "y":
        break
print(f"There are {total} people coming to the party!")

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

#challenge 6
while True:
    attempts += 1
    while True:
        try:
            num = int(input("Supply a number between 10 and 20 (inclusive): "))
            break
        except ValueError:
            print("Not an integer")
    if num < 10:
        print("Too low")
    elif num > 20:
        print("Too high")
    else: break
print("Thank you")

#challenge 7
num = 10
while (num > 0):
    print(f"There are {num} green bottles hanging on the wall, {num} green bottles hanging on the wall, if if 1 green bottle should accidentally fall,")
    num -= 1
    bottles = None;
    while (bottles != num):
        while True:
            try:
                bottles = int(input("how many green bottles will be hanging on the wall? "))
                break
            except ValueError:
                print("Not an integer")
        if bottles == num: break
        else: print("No try again")
    if num != 0:
        print(f"there will be {num} green bottles hanging on the wall")
print("There are no more green bottles hanging on the wall")