class QueueWithStack:
    def __init__(self):
        self.enqueStack=[]
        self.dequeueStack=[]

    def enqueue(self,data):
        self.enqueStack.append(data)

    def dequeue(self):

        if len(self.dequeueStack)==0 and len(self.enqueStack)==0:
            raise Exception("Stack is empty")

        # Push to deque stack if dequeue is empty
        if self.dequeueStack==[]:
            while len(self.enqueStack)!=0:
                self.dequeueStack.append(self.enqueStack.pop())

        return self.dequeueStack.pop()

if __name__ == '__main__':
    queue=QueueWithStack()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
