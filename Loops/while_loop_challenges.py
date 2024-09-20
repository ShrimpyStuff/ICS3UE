# challenge 1
total = 0
while (total <=50):
    try:
        num = int(input("Input a number to add to the total: "))
        total += num
        print(f"The total is {total}")
    except ValueError:
        print("Not an integer")

del total

#challenge 2
while True:
    try:
        num = int(input("Give me a number: "))
        if num > 5:
            break
    except ValueError:
        print("Not an Integer")

#challenge 3
