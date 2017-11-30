'''
Given a picture consisting of black and white pixels,
find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W',
which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row
and same column don't have any other black pixels.
'''
'''
Time: O(2mn)
'''


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture:
            return 0
        hash_row = {}
        hash_column = {}
        for row in range(len(picture)):
            for column in range(len(picture[row])):
                if picture[row][column] == 'B':
                    if row not in hash_row:
                        hash_row[row] = 1
                    else:
                        hash_row[row] += 1
                    if column not in hash_column:
                        hash_column[column] = 1
                    else:
                        hash_column[column] += 1
        count = 0
        for row in range(len(picture)):
            for column in range(len(picture[row])):
                if picture[row][column] == 'B':
                    if hash_row[row] <= 1 and hash_column[column] <= 1:
                        count += 1
        return count


mySolution = Solution()
picture = [['W', 'W', 'B'],
           ['W', 'B', 'W'],
           ['B', 'W', 'W']]
re = mySolution.findLonelyPixel(picture)
print(re)
