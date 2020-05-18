class node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self,head=None):
		self.head = node()
		#variable   #value
	def append(self,value):
		newnode = node(value)
		temp = self.head
		while temp.next != None:
			temp = temp.next
		temp.next = newnode

	def display(self):
		totalNodes = []
		temp = self.head
		while temp.next != None:
			temp = temp.next
			totalNodes.append(temp.data)
		print(totalNodes)

	# def length(self):
	# 	temp = self.head
	# 	cnt = 0
	# 	while temp.next != None:
	# 		temp = temp.next
	# 		cnt += 1
	# 	print(cnt)

	def length(self):
		temp = self.head
		cnt = 0
		while temp.next != None:
			temp = temp.next
			cnt += 1
		return cnt

	def removeKEnd(self,k):
		diff = (self.length()-k)+1
		index = 1
		temp = self.head
		while temp.next != None:
			lastnode = temp
			temp = temp.next
			if index == diff:
				lastnode.next = temp.next
			index += 1

	def middle(self):
		temp = self.head
		cnt = 0
		nodes = []
		while temp.next != None:
			temp = temp.next
			cnt += 1
			nodes.append(temp.data)
		mid = len(nodes)//2
		return nodes[mid]

linkedList1 = linkedList(0)
linkedList1.append(1)
linkedList1.append(2)
linkedList1.append(3)
linkedList1.append(4)
linkedList1.append(5)
linkedList1.append(6)
linkedList1.display()
#linkedList1.removeKEnd(3)
e = linkedList1.middle()
print(type(e))
linkedList1.display()

