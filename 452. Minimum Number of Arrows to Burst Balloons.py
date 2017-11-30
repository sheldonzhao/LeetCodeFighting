'''
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Input:
[[10,16], [2,8], [1,6], [7,12]]
Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11
(bursting the other two balloon
'''

from sys import maxsize


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        res, end = 0, -maxsize
        points = sorted(points, key=lambda x: x[1])
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res


mySolution = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
re = mySolution.findMinArrowShots(points)
print(re)
