class Solution(object):
    def trap(self, height):
        if not height: return 0
        l, r = 0, len(height) - 1
        leftMax , rightMax = height[l], height[r]
        res = 0
        while l < r:
             # since the bottle neck is only the min height
             # if the min height is maintained we are gonna increment in the at direction  
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r] # since we've updated the left/right max this woulld be negative
        return res
                

        