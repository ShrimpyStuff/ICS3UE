#Question 2
res_1 = input("Response 1: ")
res_2 = input("Response 2: ")

print("Yesterday I wrote a " + res_1 + ". I sent it to " + res_2 + "!")
#or
print(f"Yesterday I wrote a {res_1}. I sent it to {res_2}!")

#Question 7
string = "Hemingway"
print(string.find("m"))

#Question 10
string = "It was a bright cold day in April, and the clocks were striking thirteen."
print(string.split(",")[0])

#Assignment Questions

#Question 22
string = input("Enter a string: ")
print(string[1:] + string[0]+"ay")

#Question 23
name = input("Enter your name:")
print(name + ", " + name + ", bo-b" + name[1:])
print("Banana-fana fo-f" + name[1:])
print("Fee-fi-mo-m" + name[1:])
print(name + "!")