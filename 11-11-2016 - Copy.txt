########## Understand the Problem #############################################

'''
Make a class with a few different methods to show that two different objects
are equal and one is not, so create 3 objects in total. The class is called
Motorizedbike because the methods used will determine the cc level of
three different motorized bikes and find out which two motorized bikes will
be the same and which ones are not going to be the same. Some methods will
return the mpg and cost of the bike. The cost is based on CC and the mpg is also
based on cc within a certain range. The cc will be the user input when the
object is created. The range of cc is 50 - 100.
'''

########## Plan the Solution ##################################################

# import random int to show that one of the bikes will not be the same cc as the
# others, so for the 3rd bike make it a random cc between 50 and 100.

from random import randint

# create a class that represents the methods and objects

class Motorizedbike:

# the first method will define the characteristics of the bikes based on
# the user input cc and the odd bike method will be a random int not generated
# by user input.

    def __normalBikeSchematics(self, cc, mpg, cost):
        self.cc = cc
        if cc >= 50 and cc <= 75:
            self.mpg = 50
            self.cost = "$100-$150"
            print("Your bike has " + self.cc + " cc and costs " + self.cost + \
                  " dollars")
        elif cc < 50 or cc > 100:
            self.mpg = "Your bike doesn't exist."
            self.cost = ""
        else:
            self.mpg = 40
            self.cost = "$150-$300"

# make another method that checks to see if the bikes are equal

    def __checkIfSame(self, self1, self2):
        if self == self1:
            print("Bikes 1 and 2 are the same!")
        elif self and self1 == self2:
            print("All 3 bikes are the same!")
        elif self != self2:
            print("Bike 1 and 3 are not the same")
        elif self1 != self2:
            print("Bike 2 and 3 are not the same")

# make 2 of the same objects and 1 that is completely different.

# bike1

bike1 = Motorizedbike()
bike1.cc = 56

# bike2

bike2 = Motorizedbike()
bike2.cc = 56

# bike3

bike3 = Motorizedbike()

# make the third bike cc a random integer

randomcc = randint(50, 100)
bike3.cc = randomcc
