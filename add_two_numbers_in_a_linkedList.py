class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()
    def append(self,data):
        newnode = node(data)
        cur =self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = newnode
    def display(self):
        total_nodes = []
        cur = self.head
        while cur.next!=None:
            cur = cur.next
            total_nodes.append(cur.data)
        #total_nodes = int("".join(map(str,total_nodes)))
        return total_nodes

    # def findsum(self):
    #     sum = 0
    #     cur = self.head
    #     while cur.next!=None:
    #         cur = cur.next
    #         sum+=cur.data
    #     return sum

    def reverse(self):
        cur = self.head
        prev = None
        while cur!=None:
            nextnode = cur.next
            cur.next = prev
            prev = cur
            cur = nextnode
        self.head = prev

mylist1 = linkedlist()
mylist2 = linkedlist()

mylist1.append(1)
mylist1.append(2)
mylist1.append(3)

mylist2.append(4)
mylist2.append(5)
mylist2.append(6)

print(mylist1.display())
print(mylist2.display())        
        
# print"sum of 1st linked list:",mylist1.findsum()
# print"sum of 2nd linked list:",mylist2.findsum()

mylist1.reverse()
mylist2.reverse()

print("reversal of 1st linked list:")
print(mylist1.display())
print("reversal of 2nd linked list:")
print(mylist2.display())
