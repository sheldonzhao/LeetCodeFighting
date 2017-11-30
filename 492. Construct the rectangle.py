'''
1. The area of the rectangular web page you designed must equal to the given target area.

2. The width W should not be larger than the length L, which means L >= W.

3. The difference between length L and width W should be as small as possible.
'''
import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if area <= 0:
            return None
        i = 1
        result = []
        num = math.sqrt(area)
        while i <= num:
            if area % i == 0:
                result.append([int(area / i), i])
            i = i + 1
        return result.pop()


mySolution = Solution()
re = mySolution.constructRectangle(98)
print(re)
