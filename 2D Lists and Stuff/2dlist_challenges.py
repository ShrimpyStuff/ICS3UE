#Question 1
weird = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]] #Chose a random name

#Question 2
while True:
    try:
        row = int(input("Choose a row value between 0 and 3: "))
        column = int(input("Choose a column value between 0 and 2: "))
        try:
            print(weird[row][column])
            break
        except IndexError:
            print("A number is not in index. Domain of x: {0, 1, 2},  Range of y: {0, 1, 2, 3}")
    except ValueError:
        print("Not an integer")

#Question 3
while True:
    try:
        row = int(input(f"Choose an row between 0 and 2: "))
        try: 
            print(weird[row])
            newVal = int(input("Choose a new integer value to append: "))
            weird[row].append(newVal) # Just changing the original array
            print(weird[row])
            break
        except IndexError:
            print("Row is out of bounds")
    except ValueError:
        print("Not an integer")

#Question 4

#A bunch of redundant error correction to get more descriptive errors messages.
while True:
    try:
        row = int(input("Choose a row between 0 and 3: "))
        try: 
            print(weird[row])
            column = int(input(f"Choose a column between 0 and {len(weird[row])-1}: ")) #Use fstring and len because maybe they changed the length of the row they needed
            try: 
                print(weird[row][column])
                while True:
                    question = input("Do you want to change the value? (y/n)").lower()
                    if question == "y":
                        try:
                            newVal = int(input("Choose a new integer value to replace to value: "))
                            weird[row][column] = newVal
                            print(weird[row])
                            break
                        except ValueError:
                            print("Not an integer")
                    elif question == "n":
                        break
                    else:
                        print("Not a valid option")
                break
            except IndexError:
                print("Column is out of bounds")
        except IndexError:
            print("Row is out of bounds")
    except ValueError:
        print("Not an integer")

#Question 5
sales = {"John":{"N":3056, "S":8463, "E": 8441, "W": 2694},"Tom": {"N": 4832, "S": 6786, "E":4737, "W": 3612}, "Anne":{"N":5239, "S":4802, "E": 5820, "W": 1859},"Fiona":{"N":3904, "S":3645, "E":8821, "W": 2451}}

#Question 6
while True:
    try:
        name = input("Give a name: " + str(list(sales.keys())) + ": ") #Had to convert to a string explicitly to concatenate
        region = input("Give a region: ")
        print("Current: " + str(sales[name][region]))
        while True:
            try:
                name = input("Give a name: ")
                region = input("Give a region: ")
                print("Current: " + str(sales[name][region]))
                sales[name][region] = int(input("What is the new sales data for this region: "))
                break
            except ValueError:
                print("Not a valid integer")
        print(sales[name])
        break
    except KeyError:
        print("Not a valid name or region. Maybe check your capitalization")

#Question 7
people = {}
while len(people) < 4:
    while True:
        try:
            name = input("Enter a name for a person: ")
            age = float(input("What's their age: "))
            shoe_size = float(input("Enter a shoe size: "))
            people[name] = {"age": age, "shoe_size": shoe_size}
            break
        except ValueError:
                print("Not a number")

while True:
    try:
        name = input("Enter a name to check: ")
        print(people[name])
        break
    except KeyError:
        print("Not a valid name in the list")

#Question 8
for person in people:
    print(people[person]["age"])

#Question 9
while True:
    try:
        name = input("Enter a name to delete: ")
        people.pop(name)
        break
    except KeyError:
        print("Not a valid name in the list")
print(people)