class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

# this program uses Floy's algorithm for detecting cycle!

class LinkedList:

    def has_cycle(head):
        if (head is None):
            return False
        hare = head;
        rabbit = head.next;

        while (rabbit != hare):
            if (rabbit is None or rabbit.next is None):
                return False
            hare = hare.next;
            rabbit = rabbit.next.next;
        return True
        
