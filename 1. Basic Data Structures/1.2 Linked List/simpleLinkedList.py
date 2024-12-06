#implementation of a Linked List

class Node:
    #function that initialize the node
    def __init__(self, data):
        self.data = data #we passed data as an argument
        self.next = None #and a reference with None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    #method to add a node at the beginnin in LL
    def insertAtBegin(self, data):
        newNode = Node(data) #we create newNode with the given data
        newNode.next = self.head
        self.head = newNode

    #method to add a node at the given index in LL
    def insertAtIndex(self, data, index):
        if index == 0: #if index is equal to 0 it means the node
            self.insertAtBegin(data) #is to be inserted at the begin
            return

        pos = 0 #counter initialized with 0
        current = self.head #current node equals to the head
        while current is not None and pos + 1 != index:
            pos += 1
            current = current.next
        
        if current is not None:
            newNode = Node(data)
            newNode.next = current.next
            current.next = newNode
        else:
            print("Index not present")

    #method to add a node at the end of the LL
    def insertAtEnd(self, data):
        newNode = Node(data) #we create a new node
        if self.head is None:
            self.head = newNode #check if don't have nothing in the head, if we have it add the newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = newNode
    
    #method to print the LL
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

llist = LinkedList() #create a new linked list

#add notes to the LL
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

print("Node data: ")
llist.printLL()