"""
/******************************************************************************
 *
 *  Purpose: Program for deck of cards using linkedList
 *
 *  @author  Nikhil Patil
 *  @version 1.0
 *  @since
 *
 ******************************************************************************/
 """
from Python_Program.ObjectOriented.LinkListQueue import *
import random
class CardQueue:
    def __init__(self):
        self.suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.deck = [None] * 52
        self.array = []
        self.index = 0

    def cards(self):
        print len(self.suit), len(self.rank)
        for i in range(0,len(self.rank)):
            for j  in range(0,len(self.suit)):
                self.deck[len(self.suit) * i + j] = self.rank[i]," of " ,self.suit[j]
                # print deck[len(suit) * i + j]
    # def printdeck(self):
    #     for i in range(0,len(self.deck)):
    #         print self.deck[i]


class DeckOfCardQueue(CardQueue):

    player = LinkedListQueueCalender()
    card = LinkedListQueueCalender()

    player1 = ["Player 1", "Player 2", "Player 3", "Player 4"]

    def shuffle_cards(self):
        for i in range(0,len(self.deck)):
            rand = i + int(random.random() * (len(self.deck) - i))
            temp = self.deck[rand]
            self.deck[rand] = self.deck[i]
            self.deck[i] = temp

    def addIntoQueue(self):
        for i in range(0,len(self.player1)):
            # i = player1[i]
            self.player.enqueue(self.player1[i])
        # print len(deck)
        for j in range(0,len(self.deck)):
            # print deck[j]
            self.card.enqueue(self.deck[j])


    def print_cards(self):
        for i in range(1, 5):
            self.player.dequeue()
            for j in range(0, 9):
                self.card.dequeue()


deck_obj = DeckOfCardQueue()
deck_obj.cards()
deck_obj.shuffle_cards()
deck_obj.addIntoQueue()
deck_obj.print_cards()




# class DeckOfCard:
#     player = LinkedListQueueCalender()
#     cards = LinkedListQueueCalender()
#     suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
#     rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#     array = []
#     deck = [None]*52
#     print len(suit),len(rank)
#     for i in range(0,len(rank)):
#         for j  in range(0,len(suit)):
#             deck[len(suit) * i + j] = rank[i]," of " ,suit[j]
#     # for i in range(0,len(deck)):
#     #     print deck[i]
#     player1 = ["Player 1","Player 2","Player 3","Player 4"]
#
#     for i in range(0,len(deck)):
#         rand = i + int(random.random() * (len(deck) - i))
#         temp = deck[rand]
#         deck[rand] = deck[i]
#         deck[i] = temp
#     # for i in range(0,len(player1)):
#     #     print player1[i]
#
#     for i in range(0,len(player1)):
#         # i = player1[i]
#         player.enqueue(player1[i])
#     # print len(deck)
#     for j in range(0,len(deck)):
#         # print deck[j]
#         cards.enqueue(deck[j])
#
#     # while player.is_empty() != None:
#     #     print player.dequeue()
#     #     print "-----------------------------"
#     #
#     #     for i in range(0,9):
#     #         print cards.dequeue()
#     #     print "-----------------------------"
#     for i in range(1,5):
#         player.dequeue()
#         for j in range(0,9):
#             cards.dequeue()
#     # print cards.print_queue()