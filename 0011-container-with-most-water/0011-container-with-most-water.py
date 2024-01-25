class Solution(object):
    def maxArea(self, height):
        # the maximum water the container can hold area = width * min(left, right)
        # Approach : Two pointer
        left, right = 0, len(height) - 1
        maxhold = -1
        while left < right:
            width = right - left
            minh =  min(height[left], height[right])
            area =  width * minh
            maxhold = max(area, maxhold)
            if height[left] < height[right]: #depends on the min height the water hold capacity so we move forward to figure out the maximum water capacity by incrementing...
                left += 1
            else:
                right -= 1
        return maxhold
                     