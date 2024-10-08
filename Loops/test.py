import re
monthly = 0

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
    
data()