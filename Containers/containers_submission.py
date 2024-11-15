#Question 3
attributes = {"favourite book": "The Iron Trial", "height": "~167cm", "favourite color": "\033[38:5:45mBlue\033[0m", "age": "16"}
#Question 4
while True:
    answer = input("Choose an attribute from: " + ", ".join(list(attributes.keys())) +" : ")
    try:
        print(answer + ": " + attributes[answer])
        break
    except KeyError:
        print("Not an attribute in the dictionary")

#More practice
#Question 1
country_names = ("Canada", "Monaco", "Italy", "Singapore", "Mexico")
print(country_names)
while True:
    try:
        name = input("Choose a country from the list to find it's index: ")
        print(country_names.index(name)) #Index doesn't work if list contains more than one instance but why would I have that. No countries have the same name.
        break
    except ValueError:
        print("Not a country in the list")
#Question 4
subjects = ["Math", "Science", "English", "Music", "Gym", "Computer Science"]
#Allows for multiple subjects to be deleted
print(subjects)
while True:
    try:
        question = input("Do you like all these subjects (Yes or No): ")
        # Anything that is not yes works because only yes holds value here
        if (question.lower() == "yes"):
            print(subjects)
            break
        delete = input("Which subject from above do you dislike? (case-sensitive): ")
        subjects.remove(delete)
        print(subjects)
    except ValueError:
        print("Not a valid subject")
#Question 6
colours = ["\033[31mRed\033[0m", "\033[38:5:202mOrange\033[0m", "\033[33mYellow\033[0m", "\033[32mGreen\033[0m", "\033[34mBlue\033[0m", "\033[38:5:54mIndigo\033[0m","\033[38;2;127;0;255mViolet\033[0m", "\033[36mCyan\033[0m", "\033[35mMagenta\033[0m", "\033[38;2;0;128;102mGeneric viridian\033[0m"]
#RGB ANSI CODES ARE GOATED
while True:
    try:
        start = int(input("What is your starting number between 0 and 4? "))
        end = int(input("What is your end number between 5 and 9? "))
        if (start > 5 or start < 0) or (end < 5 or end > 9):
            print("Not in range")
            continue
        print(", ".join(colours[start:end+1]))# Not inclusive of end value so add one to end
        break
    except ValueError:
        print("Not a valid number")
#Question 8
invites = []
while True:
    if (len(invites) > 3):
        #Forces 3 names before allowing you to exit
        question = input("Do you want to invite another? Yes or No: ")
        if (question.lower() == "no"):
            print(", ".join(invites))
            print("The length of invite list is " + str(len(invites)))
            break
        question = input("Name to invite to party: ")
        invites.append(question)
    else:
        question = input("Name to invite: ")
        invites.append(question)