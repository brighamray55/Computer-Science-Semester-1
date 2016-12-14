# 7-1  8-6  8-20 ########################################################
# 7-1 ####################################################################
'''
Understand: Make a pig latin translator. Basically take the first char of a
string and append it to the end of the string in a manner "ay" if it is a
vowel, "consanant + ay" if it is a consonant. This should be done using loops
somehow......
Assumptions: the strings inputted are lowercased
'''

# Plan the solution:
# first separate the string by space to add it to a list of individual
# letters for each word

a = "hello steven faggot"
b = "eat a pineapple doofus"

list1 = a.split(" ")
vowels = ["a", "e", "i", "o", "u"]
vowel_len = len(vowels)
len_list1 = len(list1)
final_list = []
# split the individual words by space to make a list of characters

for i in range(0, len_list1):
    final_list.append(list(list1[i]))
# now switch the characters around to pig latin

fin_list_len = len(final_list)

for i in range(0, fin_list_len):
    for j in vowels:
        if final_list[i][0] == j:
            final_list[i].append("a")
            final_list[i].append("y")
            final_list[i].remove([0])
            continue
        else:
            final_list[i].append(final_list[i][0])
            final_list[i].append("a")
            final_list[i].append("y")
            final_list[i].remove([0])
            continue
# for i in range(0, len_list1 -1):

print(final_list)
