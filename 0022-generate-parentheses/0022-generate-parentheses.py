class Solution(object):
    def generateParenthesis(self, n):
        # add open ; open < n
        # add close close < open 
        # base case open = close = n
        stack = []
        res = []
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop() # since stack is the global variable onvce backtracked it needs to be clean it up!
            if closeN < openN:
                stack.append(")")
                backtrack(openN ,  closeN + 1)
                stack.pop()
        backtrack(0, 0)
        return res