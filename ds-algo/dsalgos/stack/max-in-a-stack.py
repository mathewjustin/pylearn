class MainStack:
    def __init__(self):
        self.main_stack=[]
        self.max_stack=[]


    def push(self,data):
        self.main_stack.append(data);

        #first item is same in both stack
        if len(self.main_stack)==1:
            self.max_stack.append(data)
            return
        if data>self.max_stack[-1]:
            self.max_stack.append(data)
        else: #else replicate the top again. Because the largest remains same
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        self.max_stack.pop()
        return self.main_stack.pop();

    def get_max_item(self):
        return self.max_stack.pop()

if __name__ == '__main__':

    max_stack=MainStack()
    max_stack.push(12)
    max_stack.push(123)
    max_stack.push(1)
    max_stack.push(12)
    max_stack.push(1112)
    max_stack.push(1)

    print("Max item = ", max_stack.get_max_item())
            