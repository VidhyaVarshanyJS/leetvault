class Solution(object):
    def sortColors(self, nums):
        colors = [0] * 3
        # index of the color list represents the colors itself (i.e., red , blue and white)
        for num in nums:
            colors[num] += 1 # figuring out the counts of the each colors one by one
        i = 0 
        for j in range(3):
            while colors[j] >0: # until the colors are not zero 
                nums[i] = j # assign the current index 
                colors[j] -= 1 # then decrement the value count of the colors as it is visited
                i +=1 # then increment the nums one by one onnce all the counts are full filled


      
        