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