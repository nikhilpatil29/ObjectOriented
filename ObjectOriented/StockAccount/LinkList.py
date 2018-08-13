class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def insertdata(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def printList(self):
        temp = self.head
        while temp != None:
            print temp.data
            temp = temp.next

    def search(self, word):
        flag = 0
        temp = self.head
        while (temp != None):
            if (temp.data == word):
                flag = 1
            temp = temp.next
        if (flag == 0):
            return False
        else:
            return True

    def deleteword(self, word):
        if self.head.data == word:
            self.head = self.head.next

            print "word delete"


        else:
            temp = self.head.next
            prev = self.head

            while temp.data != word:
                prev = temp
                temp = temp.next

            prev.next = temp.next

    def updateList(self):
        f = open("demo.txt","w+")
        if (self.head == None):
            print "list is empty"
        else:
            temp = self.head
            while temp != None:
                f.write(temp.data)
                f.write(" ")
                temp = temp.next
