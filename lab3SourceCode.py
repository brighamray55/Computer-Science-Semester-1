# start of test import of random int from random module

from random import randint
import math

# the user gets to choose from a level

levels = ["easy", "medium", "hard"]
user_input = input("choose a level: ")

# the user will choose from 5 lovely questions

user_numofquestions = input("How many questions from 1 to 5? ")
num_of_questions = ["1", "2", "3", "4", "5"]

# start of the test of first level "easy"
# each if statement represents a new question

if user_input == levels[0]:
        correct = 0
        for i in range(1, int(user_numofquestions) + 1):
                if i == 1:
                        n1 = randint(1, 10)
                        n2 = randint(1, 10)
                        prod = n1 + n2

                        ans = input("What is %d plus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 2:
                        n1 = randint(1, 10)
                        n2 = randint(1, 10)
                        prod = n1 - n2

                        ans = input("What is %d minus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 3:
                        n1 = randint(1, 10)
                        n2 = randint(1, 10)
                        prod = n1 + n2

                        ans = input("What is %d plus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 4:
                        n1 = randint(1, 10)
                        n2 = randint(1, 10)
                        prod = n1 - n2

                        ans = input("What is %d minus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 5:
                        n1 = randint(1, 10)
                        n2 = randint(1, 10)
                        prod = n1 + n2

                        ans = input("What is %d plus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

# the results of the testing to show the user and give advice

        print("I asked you " + str(int(user_numofquestions)) +
              " questions you got " + str(int(correct)) + " right")
        if correct / int(user_numofquestions) <= 1 and\
                correct / int(user_numofquestions) > .666:
                print("You done good young lad.")
        elif correct / int(user_numofquestions) <= .666 and\
                correct / int(user_numofquestions) >= .333:
                print("Study some more!!")
        elif correct / int(user_numofquestions) < .333 and\
                correct / int(user_numofquestions) >= 0:
                print("Ask the teacher for help.")

# start of the test of the second level "intermediate"

if user_input == levels[1]:
        correct = 0
        for i in range(1, int(user_numofquestions) + 1):
                if i == 1:
                        n1 = randint(1, 25)
                        n2 = randint(1, 25)
                        prod = n1 + n2

                        ans = input("What is %d plus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 2:
                        n1 = randint(1, 25)
                        n2 = randint(1, 25)
                        prod = n1 * n2

                        ans = input("What is %d times %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 3:
                        n1 = randint(1, 25)
                        n2 = randint(1, 25)
                        prod = math.ceil(n1 / n2)

                        ans = input(
                            "What is %d divided by %d rounded up to the" +
                            "nearest whole number? " %
                            (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 4:
                        n1 = randint(1, 25)
                        n2 = randint(1, 25)
                        prod = n1 - n2

                        ans = input("What is %d minus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 5:
                        n1 = randint(1, 25)
                        n2 = randint(1, 25)
                        prod = n1 * n2

                        ans = input("What is %d times %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

# the results of the testing to show the user and give advice

        print("I asked you " + str(int(user_numofquestions)) +
              " questions you got " + str(int(correct)) + " right")
        if correct / int(user_numofquestions) <= 1 and\
                correct / int(user_numofquestions) > .666:
                print("You done good young lad.")
        elif correct / int(user_numofquestions) <= .666 and\
                correct / int(user_numofquestions) >= .333:
                print("Study some more!!")
        elif correct / int(user_numofquestions) < .333 and\
                correct / int(user_numofquestions) >= 0:
                print("Ask the teacher for help.")

# start of the test of the third level "hard"

if user_input == levels[2]:
        correct = 0
        for i in range(1, int(user_numofquestions) + 1):
                if i == 1:
                        n1 = randint(1, 25)
                        n2 = randint(1, 13)
                        prod = n1 + n2

                        ans = input("What is %d plus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 2:
                        n1 = randint(1, 145)
                        n2 = randint(1, 60)
                        prod = n1 * n2

                        ans = input("What is %d times %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 3:
                        n1 = randint(1, 445)
                        n2 = randint(-20, 25)
                        prod = math.ceil(n1 / n2)

                        ans = input(
                            "What is %d divided by %d rounded up to the" +
                            "nearest whole number? " %
                            (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 4:
                        n1 = randint(1, 10)
                        n2 = randint(-44, -1)
                        prod = n1 - n2

                        ans = input("What is %d minus %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

                if i == 5:
                        n1 = randint(1, 708093)
                        n2 = randint(-1341, 25)
                        prod = n1 * n2

                        ans = input("What is %d times %d " % (n1, n2))
                        if int(ans) == prod:
                                print("That's right, well done.\n")
                                correct = correct + 1
                        else:
                                print("No, I'm afraid the answer is %d.\n" %
                                      prod)

# the results of the testing to show the user and give advice

        print("I asked you " + str(int(user_numofquestions)) +
              " questions you got " + str(int(correct)) + " right")
        if correct / int(user_numofquestions) <= 1 and\
                correct / int(user_numofquestions) > .666:
                print("You done good young lad.")
        elif correct / int(user_numofquestions) <= .666 and\
                correct / int(user_numofquestions) >= .333:
                print("Study some more!!")
        elif correct / int(user_numofquestions) < .333 and\
                correct / int(user_numofquestions) >= 0:
                print("Ask the teacher for help.")
