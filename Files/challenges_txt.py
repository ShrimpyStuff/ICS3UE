import os

#os.path.dirname(__file__) returns the directory of the file so that I can save the file in the same directory as the script

# Question 2
names = open(os.path.dirname(__file__) + "/Names.txt", "w")
nameArray = ["Max", "Sajid", "Ian", "Jack", "Ibrahim"]
names.write("\n".join(nameArray)) #Easy way to write each name on a new line but I will need to remove the newline character when reading
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
while True: #Probably shouldn't keep closing and opening the file and instead use file1.flush()
    #Added an exit clause so that they can accesss the menu again if they show an error or if they try it out of order
    try:
        option = int(input("1) Create a new file\n2) Display the file\n3) Add a new item to the file\n4) Exit\n\nMake a selection 1, 2, 3, or 4: "))
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

            # Display the file again with the new item
            file1 = open(os.path.dirname(__file__) + "/Subject.txt", "r")
            print(file1.read())
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
    names.seek(0)
    name = input("Enter a name to remove from the list: ")
    namesList = [tempname.strip() for tempname in names.readlines()] #readlines() outputs a list of each line so I then just remove the offender from the list and I need to strip the newline character
    try:
        namesList.remove(name)
        names.close()
        break
    except ValueError:
        print("Not a name in the list")

names2.writelines("\n".join(namesList))
names2.close()

