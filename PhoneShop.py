total = 0;
monthly = 0;

options = {"mcbasic": {"price": 50, "storage": 2, "insurance": 1}, "average joe":{"price": 150, "storage": 8, "insurance": 5}, "rich kid pro":{"price": 800, "storage": 32, "insurance": 20}}

def phone(package):
    global total
    global monthly
    global options
    if package not in options:
        raise ValueError("Not a valid phone package")
    total += options[package]["price"]


def storageOptions():
    while True:
        try:
            global total
            global monthly
            global options
            print("This plan can get additional storage options")
            choice = input("")
            if (choice in ["no", "0"]):
                break
            elif (choice == "1"):
                total += 200
            elif (choice == "2"):
                total += 350
            else:
                raise ValueError("Not a valid choice")
            break
        except ValueError as e:
            print(e)

def extraDiamonds():
    while True:
        try:
            choice = input("Would you like extra diamonds for $200? (y or n): ").lower()
            if choice not in ["y", "n"]:
                raise ValueError("Not a valid choice")
            
            if choice != "y":
                total += 200
            break
        except ValueError as e:
            print(e)

def cloudDataBackup():
    pass

def phoneCase():
    pass

def charger():
    pass

def insurance(package):
    monthly += options[package]["insurance"]

def data():
    pass

def main():
    global total
    global monthly
    global options

    print("Welcome to the Phone Shop!")
    while True:
        try:
            tradeIn = input("Would you like to trade in a device for $40? (y or n): ").lower()
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
            
            print(total)
            break
        except ValueError as e:
            print(e)

main()