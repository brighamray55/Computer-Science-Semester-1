#4-3, 4-9, 4-13, 4-19
#4-9

#Identify the problem: The cashier wants to know how many coins that
#he should give the customer. The cashier knows beforehand how much 
#cents he needs to give the customer, but wants to give the fewest
#coins and paper possible. 

#plan the solution: 
#write a function that calculates how much of a remainder there is in 
#each monetary value so 
#def dollars(dollars):
#        input("Enter the change recieved")
#assign the remainder to a variable to be used in the next function
#        output = int(dollars / 100)
#        return int(dollars % 100)
#and then call the function. dollars()
#then make the function for quarters ro find the amount of quarters needed
#this is gonna suck
#def quarters(quarters):
#       quarters = int(dollars() / 25)
#       return quarters
#then do the functions for dimes, nickels, pennies and so forth

#implementation and testing: The testing shows values from the first 
#function but there is difficulty in assigning the remainder of the 
#previous function to the next function

#Reflection: The code almost performed as it should but variable 
#names were very confusing at times and it was a challenge to put 
#together because of that.
#Some of the values needed to be returned to use for other functions
#but it was unsuccessful

#4-3

#Identify the problem: The user must input a value into 3 variables to 
#be used in the final print function. these variables must be integers
#to be used in the mathematical calculation.

#Plan a solution: assign a user input for each of the 4 variables
#x = int(input("Enter x"))
#y = int(input("Enter y"))
#x2 = int(input("Enter a second x"))
#y2 = int(input("Enter a second y"))
#then calculate the slope
#print((y2 - y) / (x2 - x))

#implimentation and testing: The code runs perfectly!!! If there isn't a 0 in the
#denominator....

#Reflection: The code has precise variables and it runs as expected.
#I would like to make it a function in the future.

#4-13

#Identify the problem: The user enters a date with the year starting first. We
#need to fix it so that user knows the actual date. They enter 8 umbers, the year first
#the month second, and the day last. The print must show month first, day second, and
#year third

#Plan a solution: have the user input information into a string in a specific
#format
#user_input = int(input("Input the date in yyyymmdd"))
#then assign the first four chars of the string to a variable
#years = user_input[0:3]
#then get the 4th and 5th chars of the user_input and assign them to the variable
#months
#months = user_input[4:5]
#then it gets complicated, we must add if statementes for each month.
#if months == 01:
#   return "January"
#elif months == 02:
#   return "February"
#elif months == 03:
#   return "March"
#elif months == 04:
#   return "April"
#elif months == 05:
#   return "May"
#elif months == 06:
#   return "June"
#elif months == 07:
#   return "July"
#elif months == 08:
#   return "August"
#elif months == 09:
#   return "September"
#elif months == 10:
#   return "October"
#elif months == 11:
#   return "November"
#elif months == 12:
#   return "December"
#then assign the 6th and 7th digits to the variable day
#day = user_input[6:7]
#then print all the variables in the format you want,
#print("months", "day",, "year")

#implementation and testing: the code works baby!!!!!

#reflection: Since the code was ambiguous to write I am wondering if there is a way
#for you to find the date an easier way, which there is but it doesn't look like
#we were supposed to use that method...

#4-19

#Identify the problem: Assume a marathon is 25 miles long. The user wants to know
#how fast they have to run to finish the marathon in the time they want.

#Plan the solution: Ask the user for the
#Amount of time they want to run in hours, minutes, and seconds
#hours = int(input("How many hours?"))
#convert the minutes and seconds to hours for easy addition in the last print
#function
#minutes = int(input("How many minutes?)) / 60
#seconds = int(input("How many seconds?)) / 3600
#then add them up together in a string that tells the user
#how fast they need to run
#print("You need to run ", + hours + minutes + seconds + , "mph")

#Implementation and testing: The code works!!!!!!!

#Reflection: There are many ways to calculate this little function however
#assigning the right variable names to the problem made the implementation and testing
#very easy.
