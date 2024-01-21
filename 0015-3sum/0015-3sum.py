class Solution(object):
    def threeSum(self, nums):
        # sort the array and do the two pointer approach
        res = []
        nums = sorted(nums)
        # to avoid the duplicates
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            # followed by the two pointer approach
            l, r = i + 1, len(nums) - 1
            while l< r:
                currSum = a + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    res.append([a , nums[l], nums[r]])
                    # again if the left pointer(i + 1) is same as the
                    # first value then it should be increased
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res   