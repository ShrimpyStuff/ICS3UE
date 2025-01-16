import os, csv

def score(password: str):
    specialChars = "!@#$%^&*()-+~"
    score = 0
    if len(password) >= 8: score += 1
    if any(char.isupper() for char in password): score += 1 #Thank geeks for geeks for the any
    if any(char.islower() for char in password): score += 1
    if any(char.isdigit() for char in password): score += 1
    if any((char in specialChars) for char in password): score += 1

    if score <= 2:
        print("Password Rejected. Too weak")
        return -1
    elif score <= 4:
        print("This password could be improved.")
        return 0
    else:
        print("This password is strong")
        return 1


fieldnames=["userID", "password"]

while True:
    options = input("1) Create a new User ID\n2) Change a password\n3) Display all User IDs\n4) Quit\n")
    if options == "1":
        while True:
            try:
                with open(os.path.dirname(__file__) + "/passwords.csv") as csvfile:
                    reader = csv.DictReader(csvfile, fieldnames=fieldnames)

                    userId = input("Enter an userID: ").lower()
                    
                    if userId in [row["userID"] for row in reader]:
                        print("User already exists")
                        break
                    csvfile.close()
                    while True:
                        password = input("Choose a strong password: ")
                        scoreNum = score(password)
                        if scoreNum == 0:
                            option = input("Would you like to improve it? ")
                            if option in ("n", "no"): #Use a tuple as it does not need to change
                                break
                        elif scoreNum == 1:
                            break
                        else:
                            continue
                    with open(os.path.dirname(__file__) + "/passwords.csv", "a") as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writerow({"userID": userId, "password": password})
                    print("Saved to database")
                    break
            except FileNotFoundError:
                with open(os.path.dirname(__file__) + "/passwords.csv", "a") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
    elif options == "2":
        userId = input("Input a userID to change the password of: ").lower()
        with open(os.path.dirname(__file__) + "/passwords.csv", "r") as csvfile: #To update the specific line I have to overwrite the file and write the ammended data
            reader = list(csv.DictReader(csvfile))
            if userId not in [row["userID"] for row in reader]:
                print("User not found")
                continue
        with open(os.path.dirname(__file__) + "/passwords.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if row["userID"] != userId:
                    writer.writerow(row)
                else:
                    while True:
                        password = input("Choose a strong password: ")
                        scoreNum = score(password)
                        if scoreNum == 0:
                            option = input("Would you like to improve it? ")
                            if option in ("n", "no"): #Use a tuple as it does not need to change
                                break
                        elif scoreNum == 1:
                            break
                        else:
                            continue
                    writer.writerow({"userID": userId, "password": password})
                    print("Updated")

    elif options == "3":
        with open(os.path.dirname(__file__) + "/passwords.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            userIds = [row["userID"] for row in reader]
            print(f"The users in the database are: {", ".join(userIds)}")
    elif options == "4":
        break
    else:
        print("Not an option")