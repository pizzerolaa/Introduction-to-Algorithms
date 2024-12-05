#implementation of a Linked List

class Node:
    #function that initialize the node
    def __init__(self, data):
        self.data = data #we passed data as an argument
        self.next = None #and a reference with None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    #method that inserts a node at the beginnin in LL
    def insertAtBegin(self, data):
        newNode = Node(data) #we create newNode with the given data
        if self.head is None: #check if the head is an empty node or not
            self.head = newNode #we make the newNode as head
            return
        else:
            newNode.next = self.next #we insert the head at the next newNode 
            self.head = newNode #and make the head equal to newNode 

    #method that inserts the node at the given index in LL
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

    def insertAtEnd(self, data):
        pass
    