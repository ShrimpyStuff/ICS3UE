#Question 1
camus = "camus"
for x in camus:
    print(x)

#Question 2
res_1 = input("Response 1: ")
res_2 = input("Response 2: ")

print("Yesterday I wrote a " + res_1 + ". I sent it to " + res_2 + "!")
#or
print(f"Yesterday I wrote a {res_1}. I sent it to {res_2}!")

#Question 3
string = "aldous Huxley was born in 1894."
print(string[0].capitalize() + string[1:])

#Question 4
string = "Where now? Who now? When now?"
cut = [sec.strip() + "?" for sec in string.split("?") if sec]
print(cut)

#Question 5
fox_list = ["The", "fox", "jumped", "over", "the", "fence", "."]
print(" ".join(fox_list[0:-1]) + fox_list[-1])

#Question 6
string = "A screaming comes across the sky."
print(string.replace("s", "$"))

#Question 7
string = "Hemingway"
print(string.find("m"))

#Question 8
dialogue = """Sajid
Died
When
He
Drank
Poison"""
print(dialogue)

#Question 9
print("three "+ "three " + "three")
print(("three " * 3).trim())

#Question 10
string = "It was a bright cold day in April, and the clockswere striking thirteen."
print(string.split(",")[0])