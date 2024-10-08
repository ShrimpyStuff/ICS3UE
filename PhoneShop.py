import re

total = 0;
monthly = 0;

options = {"mcbasic": {"price": 50, "storage": 2, "insurance": 1}, "average joe":{"price": 150, "storage": 8, "insurance": 5}, "rich kid pro":{"price": 800, "storage": 32, "insurance": 20}}

def phone(package):
    global total
    global monthly
    global options
    if package not in options:
        raise Exception("Not a valid phone package")
    total += options[package]["price"]


def storageOptions():
    while True:
        try:
            global total
            global monthly
            global options
            print("This plan can get additional storage options")
            choice = input("Would you like an additional 64GB for $200, Additional 128GB for $350?\nType 1 for 64GB, type 2 for 128GB, or type 0 or No to stick with the default amount: ").lower()
            if (choice in ["no", "0"]):
                break
            elif (choice == "1"):
                total += 200
            elif (choice == "2"):
                total += 350
            else:
                raise Exception("Not a valid choice")
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

def extraDiamonds():
    global total
    while True:
        try:
            choice = input("Would you like extra diamonds for $200? (Y or N): ").lower()
            if choice not in ["y", "n"]:
                raise Exception("Not a valid choice")
            
            if choice == "y":
                total += 200
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

def cloudDataBackup():
    global total
    while True:
        try:
            choice = input("Would you like to add cloud data backup? Data backup costs $20 for 1 year and $35 for 2 years?\nSelect 0 or no for no backup, 1 for 1 year, or 2 for 2 years: ").lower()
            if (choice in ["no", "0"]):
                break
            elif (choice == "1"):
                total += 20
            elif (choice == "2"):
                total += 35
            else:
                raise Exception("Not a valid choice")
            while True:
                try:
                    email = input("Please enter an email to register the cloud backup: ")
                    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                        raise Exception("Not a valid email")
                    break
                except Exception as e:
                    print(f"\033[91mError: {e}\033[0m")
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

def phoneCase():
    global total
    while True:
        try:
            choice = input("Choose a phone case from the following\nNo Case, \nRubber($20),\nCarbon Fibre($100)\nEnter Selection Here:").lower()
            if (choice == "no case"):
                break
            elif (choice == "rubber"):
                total += 20
            elif (choice == "carbon fibre"):
                total += 100
            else:
                raise Exception("Not a valid choice")
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

def charger():
    global total
    while True:
        try:
            choice = input("Would you like an extra fast battery charger for $100? (Y or N): ").lower()
            if choice not in ["y", "n"]:
                raise Exception("Not a valid choice")
            
            if choice == "y":
                total += 100
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

def insurance(package):
    global monthly
    while True:
        try:
            choice = input(f"Would you like insurance on this phone for ${options[package]["insurance"]} per month? (Y or N): ").lower()
            if choice == "y":
                monthly += options[package]["insurance"]
            elif choice != "n":
                raise Exception("Not a valid choice")
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

def data():
    global monthly
    while True:
        try:
            #This text is going to take sooo long to write and I really don't want to make a list for it
            print("We've started to offer data plans!")
            data = ["Pay as you go ($0)", "1 GB ($10)", "2 GB ($15)", "5 GB ($40)", "20 GB ($150)"]
            choice = input(f"Our plans are listed below:\n{"\n".join(data)}\nEnter your selection:").lower()
            
            if choice == "pay as you go":
                monthly += 0
            elif choice == "1 gb":
                monthly += 10
            elif choice == "2 gb":
                monthly += 15
            elif choice == "5 gb":
                monthly += 40
            elif choice == "20 gb":
                monthly += 150
            else:
                raise Exception("Not a valid selection")
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")
            
def main():
    global total
    global monthly
    global options

    print("Welcome to the Phone Shop!")
    while True:
        try:
            tradeIn = input("Would you like to trade in a device for $40? (Y or N): ").lower()
            if tradeIn == "y":
                total -= 40
            package = input("Choose a phone package from the following\nMcBasic($50),\nAverage Joe($150),\nRich Kid Pro($800)\nEnter Selection Here: ").lower()
            phone(package)
            print(f"This package comes with {options[package]["storage"]}GB of storage")
            if package != "mcbasic":
                storageOptions()
                if package == "rich kid pro":
                    extraDiamonds()
                cloudDataBackup()
            phoneCase()
            charger()
            insurance(package)
            data()
            
            print(f"\033[92mYour total for today is \033[1m${total}\033[0m")
            print(f"\033[96mYour monthly cost comes to a total of \033[1m${monthly}\033[0m")
            break
        except Exception as e:
            print(f"\033[91mError: {e}\033[0m")

main()

# ANSI escape colours go hard