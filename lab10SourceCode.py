# need to make a class named Card
# need to make a class named Chip Bank
# ace is equal to 1
# 1-13 = spades 14-26 = hearts 27-39 = clubs 40-52 = diamonds


'''
Class Card
    needs to represent a single card
    must use __init__(card_num)
         card_num

'''

card_face = ""


# beginning of the first class

class CardBaby():

# give the object its values

    def __init__(self, card_num):
        self.name = ""
        self.card_num = card_num
        # card_dictionary = {}
        # self.name = name
        # card_dictionary.update({name: card_num})
        if self.card_num <= 13:
            self.suit = "Spades"
            if self.card_num == 1:
                self.name = "Ace"
                self.value = "11"
            elif self.card_num == 2:
                self.name = "2"
                self.value = self.name
            elif self.card_num == 3:
                self.name = "3"
                self.value = self.name
            elif self.card_num == 4:
                self.name = "4"
                self.value = self.name
            elif self.card_num == 5:
                self.name = "5"
                self.value = self.name
            elif self.card_num == 6:
                self.name = "6"
                self.value = self.name
            elif self.card_num == 7:
                self.name = "7"
                self.value = self.name
            elif self.card_num == 8:
                self.name = "8"
                self.value = self.name
            elif self.card_num == 9:
                self.name = "9"
                self.value = self.name
            elif self.card_num == 10:
                self.name = "10"
                self.value = self.name
            elif self.card_num == 11:
                self.name = "Jack"
                self.value = 10
            elif self.card_num == 12:
                self.name = "Queen"
                self.value = 10
            elif self.card_num == 13:
                self.name = "King"
                self.value = 10
        elif self.card_num <= 26:
            self.card_num -= 13
            self.suit = "Hearts"
            if self.card_num == 1:
                self.name = "Ace"
                self.value = "11"
            elif self.card_num == 2:
                self.name = "2"
                self.value = self.name
            elif self.card_num == 3:
                self.name = "3"
                self.value = self.name
            elif self.card_num == 4:
                self.name = "4"
                self.value = self.name
            elif self.card_num == 5:
                self.name = "5"
                self.value = self.name
            elif self.card_num == 6:
                self.name = "6"
                self.value = self.name
            elif self.card_num == 7:
                self.name = "7"
                self.value = self.name
            elif self.card_num == 8:
                self.name = "8"
                self.value = self.name
            elif self.card_num == 9:
                self.name = "9"
                self.value = self.name
            elif self.card_num == 10:
                self.name = "10"
                self.value = self.name
            elif self.card_num == 11:
                self.name = "Jack"
                self.value = 10
            elif self.card_num == 12:
                self.name = "Queen"
                self.value = 10
            elif self.card_num == 13:
                self.name = "King"
                self.value = 10
            self.card_num += 13
        elif self.card_num <= 39:
            self.card_num -= 26
            self.suit = "Clubs"
            if self.card_num == 1:
                self.name = "Ace"
                self.value = "11"
            elif self.card_num == 2:
                self.name = "2"
                self.value = self.name
            elif self.card_num == 3:
                self.name = "3"
                self.value = self.name
            elif self.card_num == 4:
                self.name = "4"
                self.value = self.name
            elif self.card_num == 5:
                self.name = "5"
                self.value = self.name
            elif self.card_num == 6:
                self.name = "6"
                self.value = self.name
            elif self.card_num == 7:
                self.name = "7"
                self.value = self.name
            elif self.card_num == 8:
                self.name = "8"
                self.value = self.name
            elif self.card_num == 9:
                self.name = "9"
                self.value = self.name
            elif self.card_num == 10:
                self.name = "10"
                self.value = self.name
            elif self.card_num == 11:
                self.name = "Jack"
                self.value = 10
            elif self.card_num == 12:
                self.name = "Queen"
                self.value = 10
            elif self.card_num == 13:
                self.name = "King"
                self.value = 10
            self.card_num += 26
        elif self.card_num <= 52:
            self.suit = "Diamonds"
            self.card_num -= 39
            if self.card_num == 1:
                self.name = "Ace"
                self.value = "11"
            elif self.card_num == 2:
                self.name = "2"
                self.value = self.name
            elif self.card_num == 3:
                self.name = "3"
                self.value = self.name
            elif self.card_num == 4:
                self.name = "4"
                self.value = self.name
            elif self.card_num == 5:
                self.name = "5"
                self.value = self.name
            elif self.card_num == 6:
                self.name = "6"
                self.value = self.name
            elif self.card_num == 7:
                self.name = "7"
                self.value = self.name
            elif self.card_num == 8:
                self.name = "8"
                self.value = self.name
            elif self.card_num == 9:
                self.name = "9"
                self.value = self.name
            elif self.card_num == 10:
                self.name = "10"
                self.value = self.name
                self.value = self.name
            elif self.card_num == 11:
                self.name = "Jack"
                self.value = 10
            elif self.card_num == 12:
                self.name = "Queen"
                self.value = 10
            elif self.card_num == 13:
                self.name = "King"
                self.value = 10
            self.card_num += 39
        else:
            print("This card doesn't exist")

# return the values determined in the init method

    def get_suit(self):
        return str(self.suit)

    def get_rank(self):
        return str(self.name)

    def get_value(self):
        return str(self.value)

# determine if the card will be shown in the test code

    def face_up(self):
        global card_face
        card_face = str(self.name + " of " + self.suit)
        return card_face

    def face_down(self):
        global card_face
        card_face = "<facedown>"
        return card_face

# display the card if it is not face down

    def __str__(self):
        global card_face
        if card_face != "<facedown>" and self.card_num > 0:
            return (str(self.name) + " of " + str(self.suit))
        elif card_face == "<facedown>" and self.card_num > 0:
            return "<facedown>"

# start of the chipBank class


class ChipBank():

# determine starting value

    def __init__(self, chipValue):
        self.value = chipValue

# withdraw as much as test code permits

    def withdraw(self, amount):
        if self.value - amount < 0:
            extra = -1 * (self.value - amount)
            amount_withdrawn = amount - extra
            self.value -= amount_withdrawn
            return amount_withdrawn
        else:
            self.value -= amount
            return amount

# deposit value from test code

    def deposit(self, amount):
        self.value += amount

# displays the final total in terms of chips with different values

    def __str__(self):
        blacks = int(self.value / 100)
        remainder_after_blacks = self.value % 100
        greens = int(remainder_after_blacks / 25)
        remainder_after_greens = remainder_after_blacks % 25
        reds = int(remainder_after_greens / 5)
        remainder_after_reds = remainder_after_greens % 5
        blues = remainder_after_reds
        return (str(blacks) + " blacks " + str(greens) + " greens " +
                str(reds) + " reds " + "and " + str(blues) +
                " blues, totaling " + str(self.value))
'''
Ace = CardBaby(1)
print(Ace.get_value())

Card = CardBaby(52)
print(Card.name)
print(Card.card_num)
print(Card.get_value())

Card.face_up()
print(Card)
'''

# the start of the test code

import random
if __name__ == "__main__":
    deck = []
    for i in range(1, 53):
        mycard = CardBaby(i)
        deck.append(mycard)
        print(mycard)
    print(random.choice(deck))
    card = CardBaby(37)
    print(card)
    print(card.get_value())
    print(card.get_suit())
    print(card.get_rank())
    card.face_down()
    print(card)
    card.face_up()
    print(card)
    cs = ChipBank(149)
    print(cs)
    cs.deposit(7)
    print(cs.value)
    print(cs)
    print(cs.withdraw(84))
    print(cs)
    cs.deposit(120)
    print(cs)
    print(cs.withdraw(300))
