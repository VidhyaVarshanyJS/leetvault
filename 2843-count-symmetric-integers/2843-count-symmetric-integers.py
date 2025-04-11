class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count = 0
        for num in range(low, high+1):
            s = str(num)
            if len(s) % 2 ==0:
                mid = len(s) //2
                if sum(map(int, s[mid:]))==sum(map(int,s[:mid])):
                    count+=1
        return count



        