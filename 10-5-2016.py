'''
# 1  #########################################
a = [1, 10, 14]
print(a[0])
print(a[-1])

1, 14

'''
'''
#  2  #########################################
a = [1, 10, 14]
a.insert(2, 11)
print(a.reverse())

14, 11, 10, 1

'''
'''
# 3  ##################################################
a = ["potatoes", "onions"]
print(a[0][1:3])

"pot"

'''
'''
# 4  ############################################
a = {2, 3, 3, 4}
print(len(a))

4

'''
'''
# 5  ###############################
a = ["c", 1, "a", 3.14]
a.sort()
print(a)

error

'''
'''
# 6  #########################################
a = (1, 10, 14)
a[0] = 2
print(a[0])
print(a[-1])

2, 14

'''
'''
# 7  ###########################################
a = [{"name": "Bella Swan", "race": "Vampire"},
     {"name": "Jacob Black", "race": "Werewolf"}]
print(a[1])

name: Jacob Black, race: Werewolf

'''
'''
# 8  #######################################
a = {"name": "Clark Kent", "identity": "Superman"}
a = ["identity"] = "Green Lantern"
a = ["name"] = "Hal Jordan"
print(a)

name: Hal Jordan, Identity: Green Lantern

'''
'''
################  9  ####################################
todos = ["Wash Car", "Do Homework", "Get Bread"]
todos.append("Get Jelly")
del todos[1]
todos.sort()

Get Bread, Get Jelly, Wash car

'''
'''
# 10  ######################################
a = [{"name": "Bella Swan", "race": "Vampire"},
     {"name": "Jacob Black", "race": "Werewolf"}]
print(len(a[0]["name"]))

10

'''
'''
# 1  ###################################################
UNDERSTAND THE PROBLEM: Change a user input with more than 1 value to a list of
numbers then remove the smallest value. What happens when you're tryna take the
max of the list or there are more numbers?
'''

'''
# PLAN THE SOLUTION: (A) The user must input values and we have to convert them
# to integers with map int

user_input = input("What are your numbers?: ")
nums = list(map(int, user_input.split(",")))

# (B) see if the code runs with print

print(max(nums))
'''

'''
WHAT HAPPENS WHEN YOU ADD MORE NUMBERS? The code works the exact same as if you
had more numbers and changing the min to max finds the max instead of the min,
it is not complex
'''

'''
# 2  #############################################################
UNDERSTAND THE PROBLEM: The user finds if the value in one list is in another
list. We can find this out by using if statements possibly.
'''

'''
# PLAN THE SOLUTION:
#    (A) We will set up two arrays in a user_input for the user
# to create themselves.

user_input1 = input("What you want in your list filthy boy?: ")

# (B) map the user input as a list with string values

user_input1 = list(map(str, user_input1.split(",")))

# (C) Do the same fraking thing dummy for the second list

user_input2 = input("What you want in your list filthy boy?: ")

user_input2 = list(map(str, user_input2.split(",")))

# (D) make a repeating if statement to find something from both list_of_totals


def same_list(user_input1, user_input2):
    for i in range(0, len(user_input1)):
        if user_input1[i] in user_input2:
            print("True")
        else:
            print("False")

# (E) Run the function to see if it works

print(same_list(user_input1, user_input2))

# HELL YAH IT WORKS!!!!!!!!!!!
'''

# 3  #####################################################
'''
UNDERSTAND THE PROBLEM: The user inputs their class level, function returns the
amount of credits necessary for the user's graduation. No if statements though
so we have to uppercase the user input and assign each uppercased variable and
lowercased variable
'''

'''
# PLAN THE SOLUTION: (A) Make an array with the values for each class level

class_level = ["freshman", "sophomore", "junior", "senior"]

# (B) prompt the user to enter their class

user_input = input("Enter your class level: ")

# (C) change the input to match the array

user_input = user_input.lower()

# (D) write the function to tell them how many credits they need.


def find_credits(user_input):
    if user_input == class_level[0]:
        print("400 credits")
    elif user_input == class_level[1]:
        print("444 credits")
    elif user_input == class_level[2]:
        print("1 credits")
    elif user_input == class_level[3]:
        print("55 credits")

# (E) print the function with function call

print(find_credits(user_input))
'''

# Harambe, creator of python, approves of this function
