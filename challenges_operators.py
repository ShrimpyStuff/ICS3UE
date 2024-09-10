challengeNum = input("Run challenge [int or inta (such as 5b)]:")

def f1():
    str1 = "abc"
    str2 = "def"
    str3 = "ghi"

    print(str1)
    print(str2)
    print(str3)

    print("or")

    print(str1, str2, str3, sep="\n")

def f2():
    num1 = int(input("Give me an Integer:"))
    if (num1 < 10):
        print(num1, "is less than or equal to (≤) 10")
    else:
        print(num1, "is greater than or equal to (≥) 10")

def f3():
    num2 = int(input("Give me an Integer:"))
    if (num2 <= 10):
        print(num2, "is less than or equal to (≤) 10")
    elif (num2 <= 25):
        print(num2, "is less than or equal to (≥) 25 but greater than 10")
    else:
        print(num2, "is greater than (>) 25")

def f4():
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
    print(num1 % num2)

def f5():
    num1 = int(input("number 1:"))
    num2 = int(input("number 2:"))
    print(num1 / num2)

def f6():
    age = int(input("Input an age:"))
    if (age < 13):
        print("Get off Social Media")
    elif (30 <= age < 60 ):
        print("You might be getting old. Probably invest in some stock options for your RRSP")
    else:
        print("You might regret not investing in your retirement fund")

def f7():
    num1 = int(input("number 1:"))
    evenness = num1 % 2
    if (evenness == 0):
        print(num1, "is even")
    else:
        print(num1, "is odd")

#probably more like 5b
def f7b():
    num1 = int(input("Numerator:"))
    num2 = int(input("Denominator:"))
    try:
        print(num1 / num2)
    except ZeroDivisionError as e:
        print("invalid input.")

def f8():
    initalPop = 10000
    years = int(input("Number of years for growth:"))
    print(initalPop*(1.1**years))

try:
    funcName = locals()[f"f{challengeNum}"]
    funcName()
except KeyError:
    print("Not a valid function/challenge")