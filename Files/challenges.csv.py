import os, csv

#Question 1
with open(os.path.dirname(__file__) + "/Books.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["","Book", "Author", "Year Released"])
    writer.writerow(["0", "To Kill a Mockingbird", "Harper Lee", "1960"])
    writer.writerow(["1", "A Brief History of Time", "Stephen Hawking", "1988"])
    writer.writerow(["2", "The Great Gatsby", "F. Scott Fitzgerald", "1922"])
    writer.writerow(["3", "The Man Who Mistook His Wife for a Hat", "Oliver Sacks", "1985"])
    writer.writerow(["4", "Pride and Prejudice", "Jane Austen", "1813"])

#Question 2
with open(os.path.dirname(__file__) + "/Books.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    name = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    while True:
        try:
            year = int(input("Enter the year the book was released: "))
            break
        except ValueError:
            print("Please enter a valid year")

    with open(os.path.dirname(__file__) + "/Books.csv", "a") as writefile:
        writer = csv.writer(writefile, delimiter=",")
        csvfile.seek(0)
        writer.writerow([sum(1 for line in reader)-1, name, author, year])
    csvfile.seek(0)
    next(reader)  # Skip the header row
    for line in reader:
        print(line)

# Question 3
while True:
    try:
        numTries = int(input("Enter the number of entries to add: "))
        for i in range(numTries):
            name = input("Enter the name of the book: ")
            author = input("Enter the name of the author: ")
            year = int(input("Enter the year the book was released: "))

            with open(os.path.dirname(__file__) + "/Books.csv", "a+") as writefile:
                writefileread = csv.reader(writefile, delimiter=",")
                writer = csv.writer(writefile, delimiter=",")
                writefile.seek(0)
                writer.writerow([sum(1 for line in writefileread)-1, name, author, year])
        break
    except ValueError:
        print("Please enter a valid number")
        continue

# Read a specific column using the header value.
with open(os.path.dirname(__file__) + "/Books.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile) #DictReader is so cool
    authorName = input("Enter the author's name to check: ")
    column_name = "Author"
    
    instances = [row for row in reader if row[column_name] == authorName]
    if len(instances) == 0:
        print("No books in the database by that author")
    else:
        print(", ".join([instance["Book"] for instance in instances]))
        

# Question 4
while True:
    try:
        startYear = int(input("Enter the start year (included): "))
        endYear = int(input("Enter the end year (included): "))
        if startYear > endYear:
            print("Please enter a valid range")
            continue
        else:
            with open(os.path.dirname(__file__) + "/Books.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)
                column_name = "Year Released"
                # Change all years to ints before this to make sure this int will always be true and not throw an error
                instances = [row for row in reader if startYear <= int(row[column_name]) <= endYear] # Check range here
                if len(instances) == 0:
                    print("No books in the database during those years")
                else:
                    print(", ".join([f"{instance["Book"]} by {instance["Author"]}" for instance in instances]))
                    break
        
    except ValueError:
        print("Please enter a valid number")