class Node:

	def __init__(self,data):
		self.data = data
		self.next = None
	# def display():
	# 	print data

class LinkedListStack:

	def __init__(self):
		self.head = None
	def isEmpty(self):
		return self.head == None

	def push(self,data):
		if self.head is None:
			self.head = Node(data)
		else:
			newNode = Node(data)
			newNode.next = self.head
			self.head = newNode
		# print self.head.data
	def pop(self):
		if self.head is None:
			return "list is empty"
		else:
			popped = self.head.data
			self.head = self.head.next
			return popped	# def pop(self):
	# 	print self.head.data
	# 	self.head = self.head.next
	def display(self):
		temp = self.head
		while(temp != None):
			print self.pop()
			temp = temp.next