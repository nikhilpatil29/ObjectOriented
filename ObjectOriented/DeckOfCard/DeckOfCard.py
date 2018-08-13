"""
/******************************************************************************
 *
 *  Purpose: Program for deck of cards
 *
 *  @author  Nikhil Patil
 *  @version 1.0
 *  @since
 *
 ******************************************************************************/
 """
import random
class Card:
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.deck = [None] * 52
        self.array = []
        # self.index = 0

    def cards(self):
        print len(self.suit), len(self.rank)
        for i in range(0,len(self.rank)):
            for j  in range(0,len(self.suit)):
                self.deck[len(self.suit) * i + j] = self.rank[i]," of " ,self.suit[j]
                # print deck[len(suit) * i + j]
    # def printdeck(self):
    #     for i in range(0,len(self.deck)):
    #         print self.deck[i]


class Deck_of_card(Card):

    def shuffle_cards(self):
        for i in range(0,len(self.deck)):
            rand = i + int(random.random() * (len(self.deck) - i))
            temp = self.deck[rand]
            self.deck[rand] = self.deck[i]
            self.deck[i] = temp

    def print_cards(self):
        print "Player 1"
        for j in range(0,9):
            print self.deck[j]

        print "Player 2"
        for j in range(9, 18):
            print self.deck[j]

        print "Player 3"
        for j in range(18, 27):
            print self.deck[j]

        print "Player 4"
        for j in range(27, 36):
            print self.deck[j]

deck_obj = Deck_of_card()
deck_obj.cards()
deck_obj.shuffle_cards()
deck_obj.print_cards()