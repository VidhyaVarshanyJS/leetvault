class Solution(object):
    def evalRPN(self, tokens):
        # define the stack 
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                a , b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                a , b = stack.pop() , stack.pop()
                stack.append(int(float(b)/ a)) #round it as well as to the zero
            else:
                stack.append(int(t))
        return stack[0]

            
