class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_to_start(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def traverse_from_start(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    def reverse(self):

        prevNode = None
        nextNode = None
        currentNode=self.head

        while currentNode is not None:
            nextNode=currentNode.nextNode
            currentNode.nextNode=prevNode
            prevNode=currentNode
            currentNode=nextNode
        self.head=prevNode

if __name__ == '__main__':

    l=LinkedList()
    l.add_node_to_start(1)
    l.add_node_to_start(2)
    l.add_node_to_start(3)
    l.add_node_to_start(4)
    l.add_node_to_start(5)
    l.add_node_to_start(6)

    l.traverse_from_start()

    l.reverse()

    l.traverse_from_start()
