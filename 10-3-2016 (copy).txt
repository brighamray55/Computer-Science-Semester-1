# PROBLEM 1  ###############################################
'''
UNDERSTAND THE PROBLEM: The user inputs a list of dollar amounts for the items
they purchased and calculates the amount of a tip they want to give the waiter
for their service on a scale of poor, good, and great. The dollar amount does
not include cents and there are only three levels of service.
'''
'''
# PLAN THE SOLUTION: (A) We need to ask the user first for the dollar amounts
# of their items and calculate the sum of that list with a prompt assigned to a
# variable.

user_input = (
    input("Make a list of each item's cost to calculate your total: "))
list_of_totals = list(map(int, user_input.split(",")))

#(B) see if this creates a list of the totals

# print(list_of_totals)

#(C) get the sum of the list of totals

sum_totals = sum(list_of_totals)

# see if this works

# print(sum_totals)

#(D) Make an array with strings that show the 3 levels of service and make if
# statements that calculate a total value that they will pay the person.

level_of_service = ["poor", "good", "great"]
user_satisfaction = input("How good was your service? ")
if user_satisfaction == level_of_service[0]:
    sum_totals = sum_totals
elif user_satisfaction == level_of_service[1]:
    sum_totals = sum_totals * 1.15
elif user_satisfaction == level_of_service[2]:
    sum_totals = sum_totals * 1.2

# check to see if the code works

print(sum_totals)

'''

'''
IMPLEMENTATION AND TESTING: The code works! Needs no revisions sweetie.

REFLECTION: Writing the function was fairly easy to do but there were a few
things that made it difficult to create. We wanted to make the program user
friendly so that they could input dollar amounts of any given amount of items
and convert the strings to a number list to be used for the function. To do
this we used list(map(int, sexyinput.split(","))) which returned the data in
a list to be used. Otherwise everything else went according to plan.
'''
# PROBLEM 2  #############################################

'''
UNDERSTAND THE PROBLEM: Like problem 1, the user inputs data but instead of
calculating the tip it is calculating the tax rate which we assume is going to
be 15% of the total.
'''

'''
# PLAN THE SOLUTION: (A) We will just use the same function from the last
# problem but the total returned will be multiplied times .15 and
# assigned to a global variable.

user_input = (
    input("Make a list of each item's cost to calculate your total tax: "))
list_of_totals = list(map(int, user_input.split(",")))
tax_of_totals = sum(list_of_totals) * .15

# test to see if it returns what we wanted

print(tax_of_totals)

#yay it works
'''

'''
IMPLEMENTATION AND TESTING: The code calculates the tax baby!!!!!!!!!!!!!!!

REFLECTION: There was no issues from getting this to work. Instead of
calculating the rate of a tip, there was instead calculated the rate of tax,
so everything that was done in the last function was done in this function as
well.
'''

# PROBLEM 3  #####################################

'''
UNDERSTAND THE PROBLEM: The user inputs data into the same array as both
problems 1 and 2 except this time the user can decide to not give a tip or not.
If statements will be used to determine if the service was tipworthy but the
tax variable will always be executed to add tax to the total. The total along
with tax will be after the tip is given.
'''

'''
# PLAN THE SOLUTION: (A) Just use the same function as the first problem to get
# a list of the totals of the items from the little baby sweet user.

user_input = (
    input("Make a list of each item's cost to calculate your total: "))
list_of_totals = list(map(int, user_input.split(",")))

# (B) Calculate the total of the list like in the beginning.

sum_totals = sum(list_of_totals)

# (C) See if the user wants to leave a tip.

tip_decision = input("Do you want to leave a tip? True or False: ")
if tip_decision == "True":

# use the tip values from the first function

    level_of_service = ["poor", "good", "great"]
    user_satisfaction = input("How good was your service? ")
    if user_satisfaction == level_of_service[0]:
        sum_totals = sum_totals * 1.1
    elif user_satisfaction == level_of_service[1]:
        sum_totals = sum_totals * 1.15
    elif user_satisfaction == level_of_service[2]:
        sum_totals = sum_totals * 1.2

elif tip_decision == "False":
    sum_totals = sum_totals

# (D) tax the customer using the function from the 2nd problem

tax_of_totals = sum(list_of_totals) * .15

# (E) Print a list of values to see if the code will run correctly

print("Your total is: " + str(float(tax_of_totals) + float(sum_totals)))
'''

'''
IMPLEMENTATION AND TESTING: The code runs and executes everything according to
plan. There were some quick issues that will be addressed in the reflection.

REFLECTION: At first the code wouldn't run because the numbers returned from
tax and sum_totals were not strings which would not allow the function to run
properly. Changing the int(tax_of_totals) + int(sum_totals) to a string
allowed the function to run according to its intended purpose.
'''
