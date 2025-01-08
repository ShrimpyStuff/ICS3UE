import os
import csv

f = open(os.path.dirname(__file__) + "/test.txt", "a")
f.write("Now the file has more content!")
f.close()

with open(os.path.dirname(__file__) + "/file.csv", 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

excel = csv.reader(open(os.path.dirname(__file__) + "/file.csv", "r"), delimiter=' ', quotechar='|')

for row in excel:
    print(row)
