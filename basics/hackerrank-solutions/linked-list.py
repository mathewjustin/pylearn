class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numberOfNodes=0;
    def addNodeAtBeginning(self, data):
        newNode = Node(data)
        self.numberOfNodes=self.numberOfNodes+1
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode;

    def addNodeAtSpecificLocation(self, data, location):
        if location>self.numberOfNodes:
            print ('Invalid position')
            return
        new_node = Node(data)
        actual_node = self.head
        previous_node = self.head
        node_counter = 0;
        while node_counter < location:
            node_counter = node_counter + 1
            previous_node = actual_node
            actual_node = actual_node.nextNode

        new_node.nextNode = actual_node;
        if location != 0:
            previous_node.nextNode = new_node;
        else:
            self.head=new_node
    # self.head=previous_node

    def traverseNode(self):
        actualNode = self.head
        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.addNodeAtBeginning(2)
    linkedList.addNodeAtBeginning(3)
    linkedList.addNodeAtBeginning(4)
    linkedList.addNodeAtBeginning(5)

    linkedList.addNodeAtSpecificLocation(99, 7)

    linkedList.traverseNode();
