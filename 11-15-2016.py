'''
# Review Notes


class Test:
    pass
x = Test()


class Ph:

    def __init__(self):
        self.y = 5
        self.printHam()

    def printHam(self):
        print("ham")
x = Ph()  # this will return printHam since it is in the init function
print x.y
print x.z  # this returns an error because z is not connected to x


class Hero:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def eat(self, food):
        if food == "apple":
            self.heath -= 100
        elif food == "ham":
            self.health += 20
Bob = Hero("Bob")
print Bob.name
print Bob.health
Bob.eat("apple")
print Bob.health  # prints 0 since he is allergic to apples
'''

# UML Diagram/Problem 9-3
'''
# Top box ####################################################################

class Lock

# Mid box ####################################################################

.value = value # the lock is three digits long from 0-9 and a string
.name = name

# Third box ##################################################################

__init__(self, name, value)

__changeValue(self, newvalue)

__openLock(self, newvalue, value)
'''

# Start of Solving problem / Problem 9-4


class Lock:

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def changeValue(self, newValue):
        self.newValue = newValue
        print(self.newValue)

    def openLock(self, guess):
        if guess == self.value or guess == self.newValue:
            print(True)
        else:
            print(False)

lock1 = Lock("lock1", "567")

# test if it prints right information

print(lock1.value)
lock1.changeValue("674")
lock1.openLock("647")
lock1.openLock("789")
lock1.openLock("674")

# The code runs properly!!!!!!
