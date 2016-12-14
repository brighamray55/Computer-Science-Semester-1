#!/usr/bin/python
'''Understand the problem: REQ - Game must have a theme smarter than a 5th
grader, game needs 10 questions and some questions have more correct answers
than others. No question can be given 2 times and they should be given in
random order. Main menu says 1) Play game 2) view credits 3) quit. Every time
the user answers a question, they have the option to quit. The user has the
option to say "quit" as an answer for each question if they want to go back to
the main menu. When user enters an invalid response, then it asks them to input
a valid response. After each question the score must be displayed.
assume once the user stats the game they will play all the way through, quit
will only be available at the end of the game(main menu). The game is going
to be a list of dictionaries with key values as both the question and answers.
The answer list for each question
'''

# Plan the Solution  #####################################################

# from random import shuffle

from random import shuffle

# Create the list of dictionaries


questions = [{"question": "Who Sailed Across the Ocean Blue?",
             "answers": ["Christopher Columbus", "James", "John",
                         "Batman"],
             "correct": "1"},

             {"question": "What year was the first independence day?",
              "answers": ["1776", "year 1776", "when the country was formed",
                          "on a good day"],
              "correct": "1"},

             {"question": "What was the slave trade called?",
              "answers": ["triangular trade"],
              "correct": "1"},

             {"question": "Who Shot Abraham Lincoln?",
              "answers": ["John Wilkes Booth", "Idiot filty"],
              "correct": "1"},

             {"question": "What color is the sky?",
              "answers": ["blue", "black", "green"],
              "correct": "2"},

             {"question": "When was google established?",
              "answers": ["1998", "1997", "2020", "1775"],
              "correct": "1"},

             {"question": "What famous mountains are in Nevada?",
              "answers": ["Sierras", "Appalacians", "Rockies",
                          "Humphrey's peak"],
              "correct": "1"},

             {"question": "How many fingers does a human have?",
              "answers": ["1", "2", "10"],
              "correct": "3"},

             {"question": "What university is in Flagstaff Arizona?",
              "answers": ["ASU", "NAU", "UA"],
              "correct": "2"},

             {"question": "What is my major?",
              "answers": ["CS", "Pottery", "Gender Studies", "Anthropology"],
              "correct": "3"}]

# The length of questions dictionary will be assigned to a variable to be used
# in a for loop

len_questions = len(questions)

# the number correct will be updated with each answer correct and reset each
# time the game restarts

correct = 0

# this is the main menu which will start the game and welcome the user. The
# Game is in another function which will be called from this one


def main_menu():
    print("Welcome to the game(Main Menu)!!!!!")
    print(" ")

# User chooses what they want to do

    user_input3 = input("What would you like to do?: play, quit, credits ")
    print(" ")
    if user_input3 == "quit":

# Main Menu will appear again if they quit

        main_menu()
    elif user_input3 == "credits":
        print("Brig and Elliot made this fun little game")
        main_menu()
    else:

# if they don't quit or view credits the game will start

        main_menu2()

correct = 0

# start of the game itself


def main_menu2():

# calling correct from global allows you to call the variable from the global
# scope

    global correct
    print("Welcome to Are you Smarter Than A First Grader!!")
    print("LETS FIND OUT!!")

# shuffle questions for user

    shuffle(questions)

# This loop will iterate until the end of the length of the questions.

    for e in range(0, len_questions - 1):

# While statement allows you to repeat an iteration of a loop if the user
# chooses an incorrect response while the range is in the range of e

        while True:
            print(questions[e]["question"])
            for i, choice in enumerate(questions[e]["answers"]):
                print(str(i + 1) + ". " + choice)
            answer = input("Choose an answer: ")
            if answer == questions[e]["correct"]:
                print("Nice Job First Grader")
                correct += 1
                print("Your current score is " + str(correct) + " /10")

# This will allow you to go to the next iteration if the answer is correctf

                e += 1
                if e > len_questions - 1:
                    return results()
                else:
                    continue

# this will simply continue on the same iteration of the loop until you answer
# the question correctly

            else:
                print("Sorry, Try again figgy.")
                correct -= 1
                continue

# this function prints the results and allows you to restart the game, view
# credits, and quit the game


def results():

# this will call correct from the global variable updated in the previous
# function to show the user what they got.

    global correct
    print("You got " + str(correct) + " questions coorect!")
    print("Thanks for playing sweet lover!~! ")
    user_input = input("What would you like to do next? quit, restart," +
                       " credits")
    if user_input == "quit":
        print("okay sweetie, have a nice day!!")
        correct = 0
        main_menu()
    elif user_input == "restart":
        correct = 0
        main_menu2()
    else:
        correct = 0
        print("Brig and Elliot made this fun little game")
        main_menu()

# this piece of code initializes the main menu so the user can start playing
# the
# game

main_menu()
