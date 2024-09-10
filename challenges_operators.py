challengeNum = int(input("Run challenge (int):"))

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
    if (num1 <= 10):
        print(num1, "is less than or equal to (≤) 10")
    else:
        print(num1, "is greater than or equal to (≥) 10")

def f3():
    num2 = int(input("Give me an Integer:"))
    if (num2 < 10):
        print(num2, "is less than (<) 10")
    elif ():
        print(num2, "is greater than or equal to (≥) 10")
    else:
        print("Hello")


try:
    funcName = locals()[f"f{challengeNum}"]
    funcName()
except KeyError:
    print("Not a valid function/challenge")