import statistics as st

assigments = {}
students = {}

def add_assigment() -> None:
    additional = True
    while additional:
        try:
            name = input("What is the title of the assignment? ")
            total = int(input("What is the test out of? (Integer) "))
            marks = {}
            choice = True
            while choice:
                try:
                    stu_name = input("What is the student's name? ").lower()
                    mark = int(input("What is their mark? (As an integer value) "))
                    if stu_name in students:
                        students[stu_name].update({name:{"percent": round(mark/total * 100, 3)}})
                    else: students[stu_name] = {name:{"percent": round(mark/total * 100, 3)}}
                    marks.update({name: round(mark/total * 100, 3)})
                    check = input("Do you want to add another student? (y/n) ").lower()
                    choice = True if (check == "yes" or check == "y") else False
                except ValueError:
                    print("Not an integer value")
            marks = list(marks.values())
            assigments[name] = {"total": total, "marks": marks, "mean": st.mean(marks), "median": st.median(marks), "mode": st.mode(marks)}
            add_check = input("Do you want to add another assignment? (y/n) ").lower()
            additional = True if (add_check == "yes" or add_check == "y") else False
        except ValueError:
            print("Not an integer value")


while True:
    choice = input("A) Add Assignment B) See all assignments C) See Student D) Exit ").lower()
    if choice == "d" or  choice == "exit":
        break
    elif choice == "a" or  choice == "add assignment":
        add_assigment()
    elif choice == "b" or choice == "see all assignments":
        for assignment in assigments:
            print(f"Assignment {assignment}: The mean of the assignment is {assigments[assignment]["mean"]}, the median of the assignment is {assigments[assignment]["median"]}, The mode of the assignment is {assigments[assignment]["mode"]}")
    elif choice == "c" or choice == "see student":
        try:
            name = input("What is the student's name? ").lower()
            for assignment in students[name]:
                print(f"Assignment {assignment}: {name}'s mark is {students[name][assignment]["percent"]}")

        except KeyError: 
            print("Not a student in the list")
    