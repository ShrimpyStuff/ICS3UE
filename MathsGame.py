import os, csv

csvfile = open(os.path.dirname(__path__) + "/mathscores.csv", "a+")

def update(name, score):
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow([name, score, 5, score/5*100])
    csvfile.flush()

def quiz():
    score = 0
    update(name, score)

def results():
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row)

def menu():
    while True:
        try:
            num = int(input("1)Take the Quiz\n2)View Results (from CSV)\n3)Exit\n"))
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
name = input("What is your name?")
menu()