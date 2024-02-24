class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")":"(", "]":"[","}":"{"}
        for c in s:
            if c in closeToOpen:
                # if c in closetoopen then we pop
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else: # if we get open parentheses then we append to the stack
                stack.append(c)
        return True if not stack else False # only if the stack is empty we return True
                        