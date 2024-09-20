#question 3
def f3():
    num = int(input("Give me an Integer:"))
    if (num <= 10):
        print(num, "is less than or equal to (≤) 10")
    elif (num <= 25): # could also be testing both sides of the case with num2 > 10 and num2 <= 25
        print(num, "is less than or equal to (≥) 25 but greater than 10")
    else:
        print(num, "is greater than (>) 25")

#question 4
def f4():
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
    print(num1 % num2)

#question 5
def f5():
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
    print(num1 / num2)

f3()
f4()
f5()