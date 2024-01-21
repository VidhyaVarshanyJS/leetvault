class Solution(object):
    def twoSum(self, numbers, target):
        # input - sorted array , output - index with 1 , using two pointer approach l,r
        l, r = 0, len(numbers)-1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return[l+1 , r+1]
        