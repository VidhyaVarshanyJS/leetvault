class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        snum = ''.join(map(str,num))
        tnum = int(snum)
        total = tnum + k
        return map(int, str(total))
        
        