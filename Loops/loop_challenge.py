#challenge 1
for x in range(11):
    print(x)

#challenge 2
name = input("What is your name? ")
for i in range(3):
    print(name)

#challenge 3
while True:
    try:
        x = int(input("Supply a number: "))
        for i in range(4):
            print(x+i)
        break
    except ValueError:
        print("Not of type Integer")

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

#challenge 5
while True:
    try:
        num = int(input("Give me a number lesser than or equal to 10: "))
        if (num <= 10):
            break
        else:
            print("Too high")
    except ValueError:
        print("Not an integer")

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

#challenge 7
while True:
    question = input("Do you want a cup of tea? ").lower()
    if question not in {"no", "n"}:
        break

print("Sorry, we have run out of tea.")