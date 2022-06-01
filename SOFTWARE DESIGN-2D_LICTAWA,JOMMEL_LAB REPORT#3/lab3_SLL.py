class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def ad(self,data): #add node at the start
        new = Node(data)
        new.next = self.head
        self.head = new

    def rem(self): #remove node at the start
        if self.head is None:
            print("Linked List is empty")
        else:
            self.head = self.head.next

    def trav(self): #traversing
        if self.head is None:
            print("Linked List is empty")
            
        else:
            print("Nodes of the SinglyLinked List: ")
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next

SLL = SinglyLinkedList()
SLL.ad(10)
SLL.ad(14)
SLL.ad(78)
SLL.rem()
SLL.trav() 