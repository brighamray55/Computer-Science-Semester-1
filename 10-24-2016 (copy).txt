# 7 - 3 for loop ###############################################
'''Understand the Problem: Use a for loop to make a certain number's cubes add
together for a total. The user can only input integers.
'''

'''
# Plan the SOLUTION:

# The loop iterates from 1 to the number plus 1.

def cubes(n):
    total = []
    for i in range(1, n + 1):
# make a variable to add the items to
        total.append(i ** 3)
    return sum(total)
# see if the function runs properly
print(cubes(45))
'''


''' Reflect and Refactor: The code works according to plan once the bugs were
worked out. Remember that when the for loop runs on a certain indentation that
it will stop if you have something else on that same indentation which has
nothing else to do with the loop. Once total was defined outside of the loop
as well as append the code was able to run according to plan.
'''


# 7 - 3 while loop  ######################################################
'''Understand the problem: Create the same function as number 1 but instead use
a while loop.
'''

'''
# Plan the solution:

# create the function like the first one

# define i

total = []


def cubed(n):
# make the while loop
    i = 0
    while i < n + 1:
        total.append(i ** 3)
        i = i + 1
    return sum(total)
# see if function works
print(cubed(9))
'''


'''Reflect and Refactor: The code ran according to plan but for some reason the
variable i had to be local for the program to run according to plan. Why this
is the way it is is unknown but ask the professor why the while loop only works
under this specific condition.
'''

# 7 - 19  ################################################################

'''Understand the problem: The program takes the number value of each letter in
a specific word and returns the total score of all the letter values inputted.
Assume the numbers are integers only. Assume that the input is lower case and
the user inputs only letters.
'''
'''
# Plan the Solution:

# Make a dictionary with all the key values as letters and their respective
# point values.

list_of_values = {"a": 1,
                  "b": 3,
                  "c": 3,
                  "d": 2,
                  "e": 1,
                  "f": 4,
                  "g": 2,
                  "h": 4,
                  "i": 1,
                  "j": 8,
                  "k": 5,
                  "l": 1,
                  "m": 3,
                  "n": 1,
                  "o": 1,
                  "p": 3,
                  "q": 10,
                  "r": 1,
                  "s": 1,
                  "t": 1,
                  "u": 1,
                  "v": 4,
                  "w": 4,
                  "x": 8,
                  "y": 4,
                  "z": 10}

# Make a list that takes in the values of the inputted letters so the max value
# can be mapped out.

total_score = []

# make a function that takes in a strings


def word_score(b):
# assign the length of b for the range limit
    len_b = int(len(b))
# create an empty list containing the characters of the string input
    word_list = list(b)
# loop through each character of the string input
    for i in range(1, len_b + 1):
        for j in range(1, 27):
            total_score.append(list_of_values[word_list[i][j]])
    return(sum(total_score)

print(word_score("thick"))

# loop through each key value to find the value of the letters inputted
'''
'''        for k, l in range(1, 27):
            total_score.append(b[j])
    return sum(total_score)e
'''

'''REFLECTION: The code does not work according to plan. The issue is an
unknown error with syntax that does not seem to want to budge. Talk to the
professor about how to make it run properly.
'''
