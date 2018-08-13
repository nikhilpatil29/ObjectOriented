class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListOfQueue:

    def __init__(self):
        # self.front = self.rear = None
        self.first = None

    def isEmpty(self):
        # return self.front == None
        return self.first == None

    def enque(self,data):
        # if self.rear == None:
        #     rear = Node(data)
        #     rear.next = None
        #     rear.data = data
        #     front = rear
        # else:
        #     temp = Node(data)
        #     self.rear.next = temp
        #     temp.data = data
        #     temp.next = None
        #     rear = temp
        newNode = Node(data)
        if self.first == None:
            self.first = newNode
            return
        tempData = self.first
        while(tempData.next != None):
            tempData = tempData.next
        tempData.next = newNode


    def deque(self):
        temp = self.first
        self.first = self.first.next
        return temp.data
        # front1 = self.front
        # data = None
        # if (front1.next != None):
        #     front1 = front1.next
        #     data =  self.front.data
        #     front = front1
        # else :
        #     front = None
        #     rear = None

    def display(self):
        tempNode = self.first
        while tempNode != None:
            print self.deque()
            tempNode = tempNode.next
        # temp = self.front
        # while(self.front != self.rear):
        #     print self.deque()
        #     self.front = self.front.next
