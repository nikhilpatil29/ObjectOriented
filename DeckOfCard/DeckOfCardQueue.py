import random
from Python_Program.ObjectOriented.LinkListQueue import *
class DeckOfCard:
    player = LinkedListQueueCalender()
    cards = LinkedListQueueCalender()
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    array = []
    deck = [None]*52
    print len(suit),len(rank)
    for i in range(0,len(rank)):
        for j  in range(0,len(suit)):
            deck[len(suit) * i + j] = rank[i]," of " ,suit[j]
    # for i in range(0,len(deck)):
    #     print deck[i]
    player1 = ["Player 1","Player 2","Player 3","Player 4"]

    for i in range(0,len(deck)):
        rand = i + int(random.random() * (len(deck) - i))
        temp = deck[rand]
        deck[rand] = deck[i]
        deck[i] = temp
    # for i in range(0,len(player1)):
    #     print player1[i]

    for i in range(0,len(player1)):
        # i = player1[i]
        player.enqueue(player1[i])
    # print len(deck)
    for j in range(0,len(deck)):
        # print deck[j]
        cards.enqueue(deck[j])

    # while player.is_empty() != None:
    #     print player.dequeue()
    #     print "-----------------------------"
    #
    #     for i in range(0,9):
    #         print cards.dequeue()
    #     print "-----------------------------"
    for i in range(1,5):
        player.dequeue()
        for j in range(0,9):
            cards.dequeue()
    # print cards.print_queue()



