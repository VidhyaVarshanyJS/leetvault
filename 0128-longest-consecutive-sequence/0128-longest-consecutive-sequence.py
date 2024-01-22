class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)== 0:
            return 0
        nums = sorted(nums)
        # initialize the counts
        cnt = 1
        hcnt = 0
        for i in range(len(nums)):
            # current number is not same as the previous one (to avoid duplicates)
            if nums[i] != nums[i - 1]:
                # check if it is the consecutive num in that set
                if (nums[i] == nums[i-1] + 1):
                    cnt += 1
                else:
                    # if not the consecutive num highest count of that set is updated for the specific set and then again for the new set the cnt is again reseted
                    hcnt = max(hcnt, cnt)
                    cnt = 1
        return max(cnt, hcnt)