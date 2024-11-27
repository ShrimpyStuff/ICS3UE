#Question 1
weird = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]

#Question 2
while True:
    try:
        row = int(input("Choose a row value between 0 and 3: "))
        column = int(input("Choose a column value between 0 and 2: "))
    except ValueError:
        print("Not an integer")
    try:
        print(weird[row][column])
        break
    except IndexError:
        print("A number is not in index. Domain of x: {0, 1, 2},  Range of y: {0, 1, 2, 3}")

#Question 3
while True:
    try:
        row = int(input("Choose an row between 0 and 2: "))
    except ValueError:
        print("Not an integer")
    try: 
        print(weird[row])
    except IndexError:
        print("Row is out of bounds")
        
    try:
        newVal = int(input("Choose a new integer value to append: "))
        weird[row].append(newVal)
        print(weird[row])
        break
    except ValueError:
        print("Not an integer")

#Question 3
while True:
    try:
        row = int(input("Choose a row between 0 and 3: "))
    except ValueError:
        print("Not an integer")
    try: 
        print(weird[row])
    except IndexError:
        print("Row is out of bounds")

    try:
        column = int(input("Choose a column between 0 and 2: "))
    except ValueError:
        print("Not an integer")
    try: 
        print(weird[row][column])
    except IndexError:
        print("Column is out of bounds")
        
    try:
        newVal = int(input("Choose a new integer value to replace to value: "))
        weird[row][column] = newVal
        print(weird[row])
        break
    except ValueError:
        print("Not an integer")

#Question 5
sales = {"John":{"N":3056, "S":8463, "E": 8441, "W": 2694},"Tom": {"N": 4832, "S": 6786, "E":4737, "W": 3612}, "Anne":{"N":5239, "S":4802, "E": 5820, "W": 1859},"Fiona":{"N":3904, "S":3645, "E":8821, "W": 2451}}

#Question 6
while True:
    try:
        name = input("Give a name: ")
        region = input("Give a region: ")
        print("Current: " + sales[name][region])
        while True:
            try:
                sales[name][region] = int(input("What is the new sales data for this region: "))
                break
            except ValueError:
                print("Not a valid integer")
        print(sales[name])
        break
    except KeyError:
        print("Not a valid name or region. Maybe check your capitalization")

#Question 7
