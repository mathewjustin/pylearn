import time


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class DoublyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    #this operation inserts item at the end of the linked list
    # so we need to manipulate tail node in O(1) running time
    def insert(self,data):

        new_node = Node(data)

        #when the list is empty
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            #There is atleast 1 item in the ds
            #keep inserting items at the end of the linked list
        else:
            new_node.previous=self.tail #Made pointer from new node's previous to current tail
            self.tail.next=new_node # Mode pointer to new node from tail's next
            self.tail=new_node # tail is resetting to new node
    #we can trvse a doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node=actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous

if __name__ == '__main__':
    linked_list=DoublyLinkedList()

    now=time.time()

    for i in range(500000):
        linked_list.insert(i)

    print('Doubly linkedlist insertion taken %ss' % str(time.time()-now))

    now = time.time()
    array = []
    for i in range(500000):
        array.insert(0,i)

    print('Array insertion taken %ss' % str(time.time()-now))
