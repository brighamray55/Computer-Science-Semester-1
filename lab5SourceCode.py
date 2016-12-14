# start of first function

import time

#.add adds values in the list

# use time.time to make the timestamp

# make each of these variables lists before the functions are called
'''
times = []
groups = []
userid_s = []
text_from_post = []
# make the book

book = [times, groups, userid_s, text_from_post]
'''
# define the post id's before they are called in the like function
book = {
    "barnabas_one": {"likes": set(), "groups": [], "userid":
                     ["BarnabasCollins"],
                     "text": [], "post_time": []},
    "barnabas_two": {"likes": set(), "groups": [], "userid":
                     ["BarnabasCollins"],
                     "text": [], "post_time": []},
    "barnabas_three": {"likes": set(), "groups": [], "userid":
                       ["BarnabasCollins"],
                       "text": [], "post_time": []},
    "casper_one": {"likes": set(), "groups": [], "userid": ["Casper"],
                   "text": [], "post_time": []}
}


def update(book, status, audience, id):
    posting_time = str(time.time())
    status = str(status)
    audience = str(audience)
    userid = str(id)
    book[userid]["post_time"].append(posting_time)
    book[userid]["text"].append(status)
    book[userid]["groups"].append(audience)
    print("Post made by " + str(book[userid]["userid"]) + " at " +
          posting_time)
    return userid + " " + posting_time

'''
#test code for the update function
update(book, "I'm a thick faggot", ["fag", "dick"], "BarnabasCollins")
update(book, "I'm a dick faggot", ["fag", "sad"], "BarnabasCollins")
print(book)
'''


def like(book, id, userid):
    userid = str(userid)
    ids = str(id)
    book[ids]["likes"].update([userid])

# Test code to see if like function works properly

# remove parenthesis from parameter once you run main

'''
like(book, "barnabas_one", "dad")
like(book, "barnabas_one", "Thick faggot")
like(book, "barnabas_one", "dad")

print(book)
'''

# start of unlike function


def unlike(book, id, userid):
    userid = str(userid)
    ids = str(id)
    book[ids]["likes"].discard(userid)


# test code to see if unlike works

'''
unlike(book, "barnabas_one", "dad")

print(book)
'''


# start of display function

def display(book, id):
    ids = str(id)
    print("Time: " + str(book[ids]["post_time"]))
    print("Groups: " + str(book[ids]["groups"]))
    likes = book[ids]["likes"]
    num_of_likes = len(likes)
    print("Likes: " + str(num_of_likes))
    print(str(book[ids]["userid"]) + " says " + str(book[ids]["text"]))

# see if the function works by running main code
'''
It should display an output like this
time
groups
likes
user id says:
text from post
'''


def main():
    update(book, "Storming the village at 9, anyone interested?",
           ["Vampires", "Ghosts"], "barnabas_one")

    time.sleep(1)

    update(book, "Can I come?", ["Vampires"], "casper_one")

    time.sleep(1)

    update(book, "Forgot to include the ghosts! LOL",
           ["Ghosts"],
           "barnabas_two")

    time.sleep(1)

    update(book, "Lots of villagers with forks here...",
                 ["Vampires", "Zombies", "Ghosts"],
                 "barnabas_three")

    like(book, "barnabas_one", "Edmund")
    like(book, "barnabas_one", "Grimm")
    like(book, "barnabas_one", "Edmund")
    like(book, "casper_one", "Edmund")
    like(book, "casper_one", "Grimm")
    like(book, "casper_one", "Harry")
    like(book, "casper_one", "Count Chocula")
    like(book, "barnabas_two", "Casper")
    like(book, "barnabas_three", "Casper")
    like(book, "barnabas_three", "Count Chocula")
    like(book, "barnabas_three", "Boo")

    unlike(book, "casper_one", "Edmund")
    unlike(book, "barnabas_three", "Casper")
    unlike(book, "casper_one", "Edmund")

    display(book, "barnabas_one")
    display(book, "barnabas_three")
    display(book, "barnabas_two")
    print (" ")
    display(book, "casper_one")
main()
