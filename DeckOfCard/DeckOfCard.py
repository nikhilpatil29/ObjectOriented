import random
class DeckOfCard:
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    array = []
    deck = [None]*52
    print len(suit),len(rank)

    for i in range(0,len(rank)):
        for j  in range(0,len(suit)):
            deck[len(suit) * i + j] = rank[i]," of " ,suit[j]
            # print deck[len(suit) * i + j]

    # for i in range(0,len(deck)):
    #     print deck[i]

    for i in range(0,len(deck)):
        rand = i + int(random.random() * (len(deck) - i))
        temp = deck[rand]
        deck[rand] = deck[i]
        deck[i] = temp
    index = 0
    # for i in range(0,len(deck)):
    #     print deck[i]
    print "Player 1"
    for j in range(0,9):
        print deck[j]

    print "Player 2"
    for j in range(9, 18):
        print deck[j]

    print "Player 3"
    for j in range(18, 27):
        print deck[j]

    print "Player 4"
    for j in range(27, 36):
        print deck[j]
#
# class DeckOfCard():
#
#     def cards(self):
#         suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
#         rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
#         array = []
#         deck = [None] * 52
#         print len(suit), len(rank)
#
# class anotherclass(DeckOfCard):
#     pass
#
# def main():
#     obj1 = DeckOfCard()
#     obj1.cards()
#     obj2 = anotherclass()
#
# if __name__=="__main__":
#     main()