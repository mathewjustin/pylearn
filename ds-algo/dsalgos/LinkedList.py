
class Node:
     def __init__(self, data):
         self.data=data
         self.nextNode=None



class LinkedLIst:

    def __init__(self):
        self.head = None
        self.numberOFNodes=0
     # Here we get o(1) constant running time complexity for insertion.
    def insert_start(self,data):

        self.numberOFNodes=self.numberOFNodes+1
        new_node = Node(data)

        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode=self.head
            self.head = new_node
 #Linear running time o(n)
    def insert_end(self,data):
        self.numberOFNodes=self.numberOFNodes+1
        new_node=Node(data)

        actual_node=self.head

        while actual_node.nextNode is not None:
            actual_node=actual_node.nextNode

        actual_node.nextNode=new_node

    def size_of_list(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node=actual_node.nextNode

    def traverse(self):
        actual_node=self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node=actual_node.nextNode

    def deleteAtHead(self):

        self.head=self.head.nextNode
        self.numberOFNodes=self.numberOFNodes-1

    def deleteAtTail(self):

        actual_node = self.head

        while actual_node.nextNode.nextNode is not None:
            actual_node=actual_node.nextNode

        actual_node.nextNode=None
        self.numberOFNodes=self.numberOFNodes-1



linked_list=LinkedLIst()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start('A String type')
linked_list.insert_start(1.232)
linked_list.insert_end(12.232)
linked_list.traverse()

print('Deleting at the front')
linked_list.deleteAtHead()
linked_list.traverse()

print('Delete at the last position')
linked_list.deleteAtTail()
linked_list.traverse()

