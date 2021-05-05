class Queue:

    def __init__(self):
        self.queue=[]
    # O(1) complexity
    def is_empty(self):
        return self.queue==[]

    #O(1) constant running time complexity
    def enqueue(self,data):
        self.queue.append(data)

    #O(N) linear running time complexity, How to solve this problem? Use linked list
    # But if we use a singly linked list then enqueue will end up having O(n) running time complexity
    # Best approach is to use a doubly linked list
    def dequeue(self):
        if self.size_queue()!=0:
            data=self.queue[0]
            del  self.queue[0]
            return data
        else:
            return -1
    #O(1) constant running time complexity
    def peek(self):
        return self.queue[0]

    #O(1) constant running time complexity, python will store the length
    def size_queue(self):
        return len(self.queue)



if __name__ == '__main__':
    queue=Queue()
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

print("Size of the queue %d" % queue.size_queue())
print("Dequeue %d" % queue.dequeue())
print("Size of the queue %d" % queue.size_queue())