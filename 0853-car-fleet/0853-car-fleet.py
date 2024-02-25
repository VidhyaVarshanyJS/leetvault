class Solution(object):
    def carFleet(self, target, position, speed):
        time = [float(target - p)/s for p, s in sorted(zip(position, speed))]
        res= cur = 0
        for t in time[::-1]: #[1 , 2, 3 ] --> after the reverse [3, 2, 1]
        # maximum speed if current > next speed ..add 1 to the res stating that's the fleet
            if t > cur:
                res += 1
                cur = t #--> 3
        return res
    