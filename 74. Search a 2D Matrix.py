'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]] or target is None:
            return False
        if target < matrix[0][0] or target > matrix[len(matrix) - 1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start, end = 0, m * n - 1,
        while start <= end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


mySolution = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
matrix1 = [[]]
matrix2 = [[-10, -8, -6, -4, -3], [0, 2, 3, 4, 5], [8, 9, 10, 10, 12]]
target = 0
re = mySolution.searchMatrix(matrix2, target)
print(re)
