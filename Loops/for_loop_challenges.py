#challenge 1a
name = input("What is your name? ")
for i in range(3):
    print(name)

#challenge 1b
name = input("What is your name? ")
while True:
    try:
        num = int(input("Give me a number: "))
        break
    except ValueError:
        print("Not an integer")
for i in range(num):
    print(name)

#challenge 2a
name = input("What is your name? ")
for x in name:
    print(x)

#challenge 2b
name = input("What is your name? ")
while True:
    try:
        num = int(input("Give me a number: "))
        break
    except ValueError:
        print("Not an integer")
for y in range(num):
    for x in name:
        print(x)

#challenge 3
while True:
    try:
        num = int(input("Give me a number between 1 and 12: "))
        if (num >= 1 and num <= 12):
            break
        else:
            print("Not between 1 and 12")
    except ValueError:
        print("Not an integer")

for x in range(12):
    print(num * (x+1))

#challenge 4
while True:
    try:
        num = int(input("Give me a number below 50: "))
        if (num < 50):
            break
        else:
            print("Not below 50")
    except ValueError:
        print("Not an integer")


for x in range(50, num-1, -1): # We love the documentation
    print(x)

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

#challenge 7
while True:
    try:
        num = int(input("How many people do you want to invite to the party? "))
        if num >= 10:
            print("Too many people")
            continue
        
        for x in range(num):
            name = input("What is their name? ")
            print(f"{name} has been invited.")
        break
    except ValueError:
        print("Not an integer")