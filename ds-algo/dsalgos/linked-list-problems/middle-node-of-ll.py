class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_start(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            new_node.nextNode=self.head
            self.head=new_node

    #O(N) linear running time complexity
    def find_middle(self):

        slowPointer=self.head
        fastPointer=self.head

        while fastPointer.nextNode and fastPointer.nextNode.nextNode:
            fastPointer=fastPointer.nextNode.nextNode
            slowPointer=slowPointer.nextNode

        return slowPointer

if __name__ == '__main__':
    list=LinkedList()
    list.insert_start(1)
    list.insert_start(2)
    list.insert_start(3)
    list.insert_start(4)
    list.insert_start(5)
    print(list.find_middle().data)