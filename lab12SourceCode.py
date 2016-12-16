import random
from random import randint

# start of the card creation class

# card face variable to determine card face

card_face = ""


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

# start of chipbank class


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
                " blues, totaling " + "$" + str(self.value))

# start of blackJack Game

# start pf the BlackjackHand class

# Understand the Problem: The first class is going to determine the hand of the
# player and not the hand of the dealer. This class will return the value of
# the hand in the str method and once that is done the next class will be
# created. The second class will be the blackjack game itself and represent the
# hands of both the dealer and the player. The first card of the dealer is
# facedown though. The player can choose to hit or stand based on the value of
# their card for as many times as the value of both cards is less than or equal
# to 21. If it is 21 the player automatically has to stand.

# Plan The Solution:

# global deck for testing

# deck = []


class BlackJack():

# this mthod starts the player with a chip stack and a deck of cards

    def __init__(self, starting_dollars):

# initialize the deck list for the blackjack object

        self.deck1 = []

        for i in range(1, 53):
            mycard = CardBaby(i)
            self.deck1.append(mycard)

# instance variables for the init class

        random.shuffle(self.deck1)
        self.hand = []
        self.dealer_hand = []
        self.bank = ChipBank(starting_dollars)
        self.wager = 0
        self.dealer_hand_value = 0
        self.hand_value = 0
        self.game_active = True
        self.random_deck_index = random.randint(1, 52)
        self.random_card = self.deck1[self.random_deck_index]

# hit is called now to avoid error "hit()" doesn't exist
# hit is called if the player chooses to HIT

    def hit(self):

        random_deck_index = random.randint(1, len(self.deck1) - 1)
        random_card = self.deck1[random_deck_index]
        self.hand.append(random_card)
        self.deck1.remove(random_card)

# test to see if this will give a value

        self.hand_value += int(random_card.value)

        print("You drew a " + str(random_card))

# the player's hand after they hit is initialized here

        str_player_hand = ""

        for i in range(len(self.hand)):

            if i == len(self.hand) - 1:
                str_player_hand += str(self.hand[i])

            else:
                str_player_hand += str(self.hand[i]) + ", "

        print("Your hand is now " + str_player_hand)

# stand is called if the player gets 21+ as their value

        if self.hand_value >= 21:
            self.stand()

# this class shows the value of the dealer's hand and determines if the
# dealer needs to draw or stop drawing.

    def stand(self):

        str_dealer_hand = ""

        for i in range(len(self.dealer_hand)):

            if i == len(self.dealer_hand) - 1:
                str_dealer_hand += str(self.dealer_hand[i])

            else:
                str_dealer_hand += str(self.dealer_hand[i]) + ", "

        print("Dealer's hand is " + str_dealer_hand)

# this will end the hand if the dealer's hand is greater than 16

        if self.dealer_hand_value > 16:

            if self.dealer_hand_value > self.hand_value or\
               self.hand_value > 21:
                print("The dealer beats you!!! Sorry, your wager is gone")
                self.end_hand("lose")
                self.game_active = False

            elif self.hand_value == 21 and (self.dealer_hand_value <
                                            21 or self.dealer_hand_value > 21):
                print("You win!")
                self.end_hand("win")
                self.game_active = False

            elif self.hand_value <= 21 and (self.hand_value >
                                            self.dealer_hand_value and
                                           (self.dealer_hand_value < 21 or
                                            self.dealer_hand_value > 21)):
                print("You win!")
                self.end_hand("win")
                self.game_active = False

# this will give the dealer a card until his hand is greater than 16

        else:

            str_dealer_hand = ""

            while self.dealer_hand_value <= 16:
                random_deck_index = random.randint(1, len(self.deck1) - 1)
                random_card = self.deck1[random_deck_index]
                print("Dealer draws " + str(random_card))
                self.dealer_hand.append(random_card)

                for i in range(len(self.dealer_hand)):

                    if i == len(self.dealer_hand) - 1:
                        str_dealer_hand += str(self.dealer_hand[i])

                    else:
                        str_dealer_hand += str(self.dealer_hand[i]) + ", "

                print("Dealer's hand is now " + str_dealer_hand)
                self.dealer_hand_value += int(random_card.value)

            if self.dealer_hand_value <= 21 and self.dealer_hand_value >\
               self.hand_value:
                print("The dealer bests your hand!")
                self.end_hand("lose")
                self.game_active = False
            elif self.dealer_hand_value > 21:
                print("The dealer busts, you win!")
                self.end_hand("win")
                self.game_active = False
            elif self.hand_value > self.dealer_hand_value and\
                    self.hand_value < 21:
                print("you win!")
                self.end_hand("win")
                self.game_active = False
            elif self.hand_value > 21:
                print("you lose!")
                self.end_hand("lose")
                self.game_active = False
            elif (self.dealer_hand_value == self.hand_value) and\
                 ((self.dealer_hand_value <= 21) and (self.hand_value <= 21)):
                print("it is a tie!")
                self.end_hand("push")
                self.game_active = False

# the execution function of the game when it first starts
# this creates a hand for the dealer and the player

    def start_hand(self, wager):
        self.wager = 0
        for i in range(2):
            random_deck_index = random.randint(1, len(self.deck1) - 1)
            random_card = self.deck1[random_deck_index]
            self.hand.append(random_card)
            self.deck1.remove(random_card)
            random_deck_index = random.randint(1, len(self.deck1) - 1)
            random_card = self.deck1[random_deck_index]
            self.dealer_hand.append(random_card)
            self.deck1.remove(random_card)

# wager instance variable

        if wager >= self.bank.value:
            self.wager = self.bank.value
            self.bank.value = 0

        else:
            self.bank.value -= wager
            self.wager = wager

        str_player_hand = ""
        str_dealer_hand = ""

        for i in range(len(self.hand)):
            if i == len(self.hand) - 1:
                str_player_hand += str(self.hand[i])

            else:
                str_player_hand += str(self.hand[i]) + ", "

#        while True:
#
#            try:
#
#                wager <= self.bank.value
#                self.wager = wager
#
#            except ValueError:
#                print("your wager is too high")

# dealer hand construction

        for i in range(len(self.dealer_hand)):

            if i == 0:
                str_dealer_hand += "<facedown>" + ", "

            else:
                str_dealer_hand += str(self.dealer_hand[i])

        print("your hand: " + str_player_hand)
        print("dealer's hand: " + str_dealer_hand)

        for i in range(len(self.hand)):
            self.hand_value += int(self.hand[i].value)

        for i in range(len(self.dealer_hand)):
            self.dealer_hand_value += int(self.dealer_hand[i].value)

# a short circuit if the player wins the game through truthiness

        if self.hand_value == self.dealer_hand_value:
            print("It is a tie!!!! Your wager is returned.")
            self.end_hand("push")
            self.game_active = False

        elif self.hand_value == 21:
            self.stand()

        elif self.hand_value < 21:
            self.game_active = True

        elif self.hand_value > 21:
            print("You bust!!!")
            self.end_hand("lose")
            self.game_active = False

# this determines if the game is active (doesn't actually do anything
# though haha)

    def game_active(self):

        if self.game_active is False:
            return False
        else:
            return True

# this will reset the hand when it is executed. The user can keep playing until
# all of their chips are gone

    def end_hand(self, outcome):

        outcome = str(outcome)

        if outcome == "win":
            self.dealer_hand_value = 0
            self.hand_value = 0
            self.hand = []
            self.dealer_hand = []
            self.bank.value += (self.wager * 2)
            self.deck1 = []

            for i in range(1, 53):
                mycard = CardBaby(i)
                self.deck1.append(mycard)

        elif outcome == "lose":
            self.dealer_hand_value = 0
            self.hand_value = 0
            self.hand = []
            self.dealer_hand = []
            self.bank.value = self.bank.value
            self.deck1 = []

            for i in range(1, 53):
                mycard = CardBaby(i)
                self.deck1.append(mycard)
        elif outcome == "push":
            self.dealer_hand_value = 0
            self.hand_value = 0
            self.hand = []
            self.dealer_hand = []
            self.bank.value += self.wager
            self.deck1 = []

            for i in range(1, 53):
                mycard = CardBaby(i)
                self.deck1.append(mycard)

# start of the test code


def main():
    if __name__ == "__main__":
        blackjack = BlackJack(250)
        while blackjack.bank.value > 0:
            print("Your remaining chips: " + str(blackjack.bank))
            wager = int(input("How much would you like to wager? "))
            blackjack.start_hand(wager)
            while blackjack.game_active is True:
                choice = input("STAND or HIT: ").upper()
                if choice == "STAND":
                    blackjack.stand()
                elif choice == "HIT":
                    blackjack.hit()
            print()
        print("Out of money! The casino wins!")
main()
