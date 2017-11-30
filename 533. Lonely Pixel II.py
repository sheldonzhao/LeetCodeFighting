'''
Given a picture consisting of black and white pixels,
and a positive integer N, find the number of black pixels located
at some specific row R and column C that align with all the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
'''


class Solution(object):
    def findBlackPixel(self, picture, N):
        """
        :type picture: List[List[str]]
        :type N: int
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
                        hash_row[row] = [column]
                    else:
                        hash_row[row].append(column)
                    if column not in hash_column:
                        hash_column[column] = [row]
                    else:
                        hash_column[column].append(row)
        count = 0
        for row in range(len(picture)):
            for column in range(len(picture[row])):
                if picture[row][column] == 'B':
                    # rule1
                    if len(hash_row[row]) == N and len(hash_column[column]) == N:
                        # rule 2
                        flag = 0
                        l = hash_column[column]
                        for i in range(len(l) - 1):
                            if picture[l[i]] != picture[l[i + 1]]:
                                flag = 1
                                break
                        if flag == 0:
                            count += 1
        return count


mySolution = Solution()
picture = [['W', 'B', 'W', 'B', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'B', 'W'],
           ['W', 'W', 'B', 'W', 'B', 'W']]
re = mySolution.findBlackPixel(picture, 3)
print(re)
