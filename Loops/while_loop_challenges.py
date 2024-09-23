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
del num

#challenge 3
total = 0;
num0 = int(input("Give me a number to add to the total: "))
total += num0
while True:
    num1 = int(input("Give me another input: "))
    total += num1
    answer = input("Do you want to enter another number (y/n): ").lower()
    if answer != "y":
        break
print(total)
del total

#challenge 4
