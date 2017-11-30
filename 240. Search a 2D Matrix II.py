'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
'''
'''
time: O(m+n)
method: start from the num of top right,
if num == target: return True
if num < target: get num toward downward
else: get num toward left
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:
            return False
        m, n = len(matrix), len(matrix[0])
        row, column = 0, n - 1
        num = matrix[row][column]
        while True:
            if num == target:
                return True
            elif num > target:
                column -= 1
            else:
                row += 1
            if row == m or column == -1:
                return False
            num = matrix[row][column]

mySolution = Solution()
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 20
re = mySolution.searchMatrix(matrix, target)
print(re)
