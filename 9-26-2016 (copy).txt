# 5-5#####################################################################

'''UNDERSTAND THE PROBLEM: The user is asked to enter 3 numbers in a prompt and
find out if the last character of each number is equal to each other number. It
is the last character of each string, and cannot be a floating point number.
The user will input each number in the function as a string'''

'''PLAN SOLUTION: We will assign each of the users input numbers to a variable
to a prompt'''

# num1 = input("Enter a number")
# num2 = input("Enter another number")
# num3 = input("Enter a final number")

'''we will make a function to determine if there is indeed a similarity
between the 3 end values of each string.'''

'''We will also tell the user beforehand how to input the parameters
print("make sure to input in string format!!!")'''


'''def discover(a, b, c):
    a = a[-1]
    b = b[-1]
    c = c[-1]
    if a == b and a == c:
        return "true"
    else:
        return "false"'''

'''IMPLEMENTATION AND TESTING: The code works perfectly! At first it was a[:-1]
but that just isolates the characters in front of the last. We figured out that
it is a[-1] to give the very last character of a string'''

'''REFLECTION: There seems to not be a way to let the user input an integer
without breaking the function for some reason. It would be less ambiguous if
the user could input a simple integer'''

# 5-6#####################################################################

'''UNDERSTAND THE PROBLEM: Like question 5-5 the user inputs 3 numbers, but
this time the user wants to find out which of the three numbers is the greatest
of them all. We can do this with if statements. There is no truthiness to this
function because the user wants to know a number'''

'''PLAN A SOLUTION: Tell the user that he needs to simply input values as a
string literal

print("Input values as a string")'''

'''Next up, create the function boss!!!'''


'''def findmidnum(a, b, c):
# be careful because you have to make these numbers integers to find the
# max
    a = int(a)
    b = int(b)
    c = int(c)
# create an array out of these numbers so you can pop off the max of the
# three
    user_input = [a, b, c]
    user_input.sort()
# pop off the max of the array
    mid_numberarray = user_input[:-1]
# now the function is only 2 numbers long with the max num as the middle
# number
    return max(mid_numberarray)'''

'''IMPLEMENTATION: The code runs great! It was difficult to get the max value
off of the end of the array, an easier way was to sort the numbers in an easier
form'''

'''REFLECTION: the pop() function is meant to pop off the last form of data in
an array, it is not specific enought to use for most cases. That held the code
back from producing the desired results in a timely manner'''

# 5-10####################################################################

'''UNDERSTAND THE PROBLEM: The user enters hours, minutes, and seconds to be
converted into seconds until midnight. This time it has to be in a function.
The user input is entered as integers not float numbers for readability.'''

'''PLAN SOLUTION: The user is inputting the value of the hours minutes and
seconds as strings into functions.'''


'''def secondsfrommidnight(a, b, c):
# convert the strings to numbers
    a = int(a)
    b = int(b)
    c = int(c)
# convert a and b into seconds
    a = a * 3600
    b = b * 60
# then add together the values for total time
    return a + b + c'''

'''IMPLEMENTATION: The code runs according to plan!!!!!!!! There were zero
reruns, it worked the very first time.'''

'''REFLECTION: Understanding the conversions from minutes and hours to seconds
was helpful in completing the problem. Since it was basically just doing 3-10
over again there were no problems in getting it to run properly.'''
