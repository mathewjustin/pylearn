
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


linked_list=LinkedLIst()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(5)
linked_list.insert_start(6)
linked_list.insert_end(10)
linked_list.traverse()
