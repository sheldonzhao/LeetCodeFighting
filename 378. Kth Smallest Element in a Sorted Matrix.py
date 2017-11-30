'''
Given a n x n matrix where each of the rows and columns are sorted in
ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,
not the kth distinct element.

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
'''

from sys import maxsize


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            min_value = maxsize
            min_row = -1
            for i in matrix:
                if i and i[0] < min_value:
                    min_value = i[0]
                    min_row = i
            min_row.pop(0)
        return min_value


mySolution = Solution()
matrix = [
    [],
    [13],
    [12, 13, 15]
]
k = 3
re = mySolution.kthSmallest(matrix, k)
print(re)
