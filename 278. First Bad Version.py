# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
'''
time: O(logN)
'''


class Solution(object):
    def isBadVersion(self, n):
        return

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if self.isBadVersion(mid):
                end = mid
            else:
                start = mid+1
        return start
