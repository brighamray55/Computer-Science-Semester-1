# Grade Calculator Lab 4
authors = "Brigham Ray and Vashtia Caldwell"
# Write code that determines the weighted average grade of the student
# to calculate weight we multiply the score by weight percent
# define main function
# call the main function in another function
# print letter grades
# calculate weighted score with letter grade

# homework totals
homework = [40, 40, 40, 40, 40, 5]
score_of_homework = [39, 40, 29, 40, 0, 5]
sum_of_homework = sum(score_of_homework)
sum_homework = sum(homework)
# print(sum_homework)
# print(sum_of_homework)

# quiz totals
quizzes = [10, 10, 10, 10, 10, 10, 10]
score_of_quizzes = [10, 10, 9, 2, 10, 10, 10]
sum_of_quizzes = sum(score_of_quizzes)
sum_quizzes = sum(quizzes)

# test totals
test = [300, 300, 300]
score_of_test = [293, 284, 300]
sum_of_test = sum(score_of_test)
sum_test = sum(test)

# function determines the percentages per each wonderful category


def percentage_per_category(sum_of_homework, sum_homework, sum_of_quizzes,
                            sum_quizzes, sum_of_test, sum_test):
    percent_homework = (sum_of_homework / sum_homework) * 100
    percent_quizzes = (sum_of_quizzes / sum_quizzes) * 100
    percent_tests = (sum_of_test / sum_test) * 100

# this checks to see if the code works
    print(percent_homework, percent_quizzes, percent_tests)

# this returns the values that will be used in the next function

    return(percent_homework, percent_quizzes, percent_tests)

# next function determines the letter grade from each category unweighted


'''
We need to assign the results of the first function to use in the second
one and to do that just assign to the variable names used in the second
function the results of the first function
'''

'''############################################################################
###############################################################################
#GLOBAL VARIABLES FOR USE IN FINAL RESULTS#####################################
###############################################################################
############################################################################'''


percent_of_each_section = (percentage_per_category(sum_of_homework,+
    sum_homework, + sum_of_quizzes, sum_quizzes, sum_of_test, sum_test))
percent_homework = percent_of_each_section[0]
percent_quizzes = percent_of_each_section[1]
percent_tests = percent_of_each_section[2]


'''############################################################################
###############################################################################
#GLOBAL VARIABLES FOR USE IN FINAL RESULTS#####################################
###############################################################################
############################################################################'''


def letter_grade(percent_homework, percent_quizzes, percent_tests):
    #This line determines the grade for homework
        if percent_homework <= 100 and percent_homework >= 90:
            homework_grade = "A"
        elif percent_homework < 90 and percent_homework >= 80:
            homework_grade = "B"
        elif percent_homework < 80 and percent_homework >= 70:
            homework_grade = "C"
        elif percent_homework < 70 and percent_homework >= 60:
            homework_grade = "D"
        else:
            homework_grade = "F"

# This line determines the grade for quizzes

        if percent_quizzes <= 100 and percent_quizzes >= 90:
            quizzes_grade = "A"
        elif percent_quizzes < 90 and percent_quizzes >= 80:
            quizzes_grade = "B"
        elif percent_quizzes < 80 and percent_quizzes >= 70:
            quizzes_grade = "C"
        elif percent_quizzes < 70 and percent_quizzes >= 60:
            quizzes_grade = "D"
        else:
            quizzes_grade = "F"

# This line determines the grade for tests

        if percent_tests <= 100 and percent_tests >= 90:
            tests_grade = "A"
        elif percent_tests < 90 and percent_tests >= 80:
            tests_grade = "B"
        elif percent_tests < 80 and percent_tests >= 70:
            tests_grade = "C"
        elif percent_tests < 70 and percent_tests >= 60:
            tests_grade = "D"
        else:
            tests_grade = "F"

# This will print the grade to see if the code works

#        print(homework_grade, quizzes_grade, tests_grade)

        return(homework_grade, quizzes_grade, tests_grade)

'''
Assign the results of this function to 3 different variables to display in a
final results column for the code checker to look at
'''

'''############################################################################
###############################################################################
#GLOBAL VARIABLES FOR USE IN FINAL RESULTS#####################################
###############################################################################
############################################################################'''


grade_results = letter_grade(
    percent_homework, percent_quizzes, percent_tests)
homework_results = grade_results[0]
quiz_results = grade_results[1]
test_results = grade_results[2]


'''############################################################################
###############################################################################
#GLOBAL VARIABLES FOR USE IN FINAL RESULTS#####################################
###############################################################################
############################################################################'''

# This function will calculate the weighted grade for each section


def weighted_score(percent_homework, percent_quizzes, percent_tests):
    weighted_homework = percent_homework * .2
    weighted_quizzes = percent_quizzes * .2
    weighted_tests = percent_tests * .6
    final_weighted_score = weighted_homework + \
        weighted_quizzes + weighted_tests
    if final_weighted_score <= 100 and final_weighted_score >= 90:
        final_weighted_grade = "A"
    elif final_weighted_score < 90 and final_weighted_score >= 80:
        final_weighted_grade = "B"
    elif final_weighted_score < 80 and final_weighted_score >= 70:
        final_weighted_grade = "C"
    elif final_weighted_score < 70 and final_weighted_score >= 60:
        final_weighted_grade = "D"
    else:
        final_weighted_grade = "F"
    return (final_weighted_score, final_weighted_grade)


'''############################################################################
###############################################################################
#GLOBAL VARIABLES FOR USE IN FINAL RESULTS#####################################
###############################################################################
############################################################################'''


# this will assign the results of this function to a variable to be used in
# final results

final_score = weighted_score(
    percent_homework, percent_quizzes, percent_tests)
final_grade = final_score[0]
final_letter_grade = final_score[1]


'''############################################################################
###############################################################################
#GLOBAL VARIABLES FOR USE IN FINAL RESULTS#####################################
###############################################################################
############################################################################'''


# This will return the string grades for the quizzes, tests, and homework

# print(letter_grade(percent_homework, percent_quizzes, percent_tests))

# This will print the results of the weighted grade function

# print(weighted_score(percent_homework, percent_quizzes, percent_tests))

# This will print the very last final results for the lab aids to checker

print("Homework Grade: " + str(int(percent_homework)) +
      " (" + str(homework_results) + ")")
print("Quiz Grade: " + str(int(percent_quizzes)) +
      " (" + str(quiz_results) + ")")
print("Test Grade: " + str(int(percent_tests)) +
      " (" + str(test_results) + ")")
print("Final Score: " + str(int(final_grade)) +
      " (" + str(final_letter_grade) + ")")
