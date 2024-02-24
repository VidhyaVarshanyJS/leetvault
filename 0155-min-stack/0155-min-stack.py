class MinStack(object):

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val):
        # just appending it to the stack
        self.stack.append(val)
        # here the second stack maintains the min value for the current insert position 
        # by comparing it with the normal new value
        val = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val)
        
    def pop(self):
        self.stack.pop()
        self.MinStack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()