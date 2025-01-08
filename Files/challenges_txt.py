import os

# Question 2
names = open(os.path.dirname(__file__) + "/Names.txt", "w")
nameArray = ["Max", "Sajid", "Ian", "Jack", "Ibrahim"]
names.write("\n".join(nameArray))
names.close()

#Question 3
names = open(os.path.dirname(__file__) + "/Names.txt", "r")
print(names.read())
names.close()

#Question 4
names = open(os.path.dirname(__file__) + "/Names.txt", "a")
name = input("Input a name: ")
names.write("\n"+name)
names.close()

names = open(os.path.dirname(__file__) + "/Names.txt", "r")
print(names.read())

#Question 5
while True:
    try:
        option = int(input("1)Create a new file\n2)Display the file\n3)Add a new item to the file\n4)Exit\n\nMake a selection 1, 2, 3, or 3 "))
        if option == 1:
            name = input("Enter a name for a subject: ")
            file1 = open(os.path.dirname(__file__) + "/Subject.txt", "w")
            file1.write(name)
            file1.close()
        elif option == 2:
            try:
                file1 = open(os.path.dirname(__file__) + "/Subject.txt", "r")
                print("\n"+file1.read()+"\n")
                file1.close()
            except:
                print("There is no file. Please try option 1 to create a new file")
        elif option == 3:
            name = input("Enter a new subject: ")
            file1 = open(os.path.dirname(__file__) + "/Subject.txt", "a")
            file1.write("\n"+name)
            file1.close()
        elif option == 4:
            break
        else:
            print("Not a valid option")
    except ValueError:
        print("Not a valid option")

#Question 6
while True:
    names = open(os.path.dirname(__file__) + "/Names.txt", "r")
    names2 = open(os.path.dirname(__file__) + "/Names2.txt", "w")
    print(names.read())
    name = input("Enter a name to remove from the list")
    namesList = names.readlines()
    try:
        namesList.remove(name)
        break
    except ValueError:
        print("Not a name in the list")

names2.writelines(namesList)

