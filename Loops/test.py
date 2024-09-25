while True:
    try:
        num = int(input("How many people do you want to invite to the party? "))
        if num >= 10:
            print("Too many people")
            continue
        
        for x in range(num):
            name = input("What is their name? ")
            print(f"{name} has been invited.")
        break
    except ValueError:
        print("Not an integer")