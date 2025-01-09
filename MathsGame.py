import os, csv, random

csvfile = open(os.path.dirname(__file__) + "/mathscores.csv", "a+")

def update(name, score):
    csvwriter = csv.writer(csvfile, delimiter=",") #Using csv writer to write to the file with proper formatting
    csvwriter.writerow([name, score, 5, score/5*100]) #Write row makess it a lot easier
    csvfile.flush()

def quiz():
    name = input("What is your name? ")
    score = 0
    for i in range(1, 6):
        print(f"Question {i}:")
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(["+", "-", "*", "/"])
        value = None
        if operator == "/":
            value = round(num1 / num2, 2)
        elif operator == "*":
            value = num1 * num2
        elif operator == "-":
            value = num1 - num2
        elif operator == "+":
            value = num1 + num2
        try:
            #Round here as well as to not punish more accurate answers even though it specifies two decimal places
            answer = round(float(input(f"What is {num1} {operator} {num2}? Answer in two decimal places. ")), 2)
            if answer == value:
                score += 1
                print("\033[38;2;0;255;0mCorrect!\033[0m")
            else:
                print(f"\033[38;2;255;0;0mNot Correct. The correct answer was {value}\033[0m")
        except ValueError:
            print("Not a valid number")
    update(name, score)

def results():
    csvread = csv.reader(csvfile, delimiter=",")
    csvfile.seek(0)
    headers = ["Name: ", "Score: ", "Out of: ", "Percentage: "]
    print("")
    for row in csvread: 
        if len(row) > 0:
            for idx, value in enumerate(row): #Get the index and the value
                print(headers[idx] + value)
            print("")

def menu():
    while True:
        try:
            num = int(input("1) Take the Quiz\n2) View Results (from CSV)\n3) Exit\n"))
            if num == 1:
                quiz()
            elif num == 2:
                results()
            elif num == 3:
                csvfile.close()
                exit(0)
            else:
                print("Not a valid option")
                continue
        except ValueError:
            print("Not a valid option")

print("Welcome to the Maths Quiz!")
menu()