'''
1)
x returns the text inside of the file that
was opended

2)
The document is opened and can be read, lines
is the lines read from the document,
x is the 2nd line of the document, fh.close
closes the document and no further changes
can be made.

3)
fh opens it for writing, fh.write puts "check
out nau" at the end of the doc, fh.close closes
the document so no further changes can be made.

4)
fh opens the doc for append, if the file doesn't exist
it will create a new one. fh.write writes check out nau at
the end of the file if it exists. fh.close closes the doc
from further editing.

5)
fh opens doc for append, x shows the text within the file
and fh closes the file in the end.

6)
fh opens file for writing, the loop writes something 3 times
and x is equal to i, fh closes the document in the end.

7)
fh opens for reading, x = to the first line of the file,
x is then equal to the length of the line, and fh closes
the document.

8)
fh opens for reading, x reads all the lines of each file,
x is equal to the length of the document character count.
fh closes the document.

9)
fh opens the file for reading and writing,
lines is equal to the lenth of the document
the loop writes i and replaces current text.
fh then closes the document

10)fh opens for reading and writing the document
lines = the entire document. the loop writes in for each
seperate line "i" replacing the current text
x is equal to a list of the first line, fh closes the doc.
'''

# 7 - 7 ##################################################################
'''Understand the Problem: There is a given grid of numbers whose rows and
columns totals must be equal to one another.
'''

# Plan the solution:

# make a dictionary with the number of row as the key value and a list of
# integers for each key value

# make the dictionary

thick = {"1": [11, 18, 25, 2, 9],
         "2": [10, 12, 19, 21, 3],
         "3": [4, 6, 13, 20, 22],
         "4": [23, 5, 7, 14, 16],
         "5": [17, 24, 1, 8, 15]}

# make empty list for each individual rows

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

# create a loop that goes through the dictionary and returns if the grid has
# the requirements

for key, value in range(1, 6):
    list1.append(thick[key][value])

# Implement and test: The program doesn't work according to plan. There is
#no way to fix it currently because I need to study how loops work since
#it is just really confusing of a concept.

#Reflect and refactor: The whole program doesn't even work so learning how
#loops work theoretically is the only way that I will have an ability to
#fix the program is to learn how loops work at all.
