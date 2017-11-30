'''
time: O(n)
mindset: f(i,j)=min(f(i,j+1)+f(i+1,j))-dungeon(i,j)
if f(i,j)<=0: f(i,j)=1
'''

from sys import maxsize


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        l = []
        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m + 1):
            l.append([maxsize] * (n + 1))
        l[m][n - 1], l[m - 1][n] = 1, 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                l[i][j] = min(l[i + 1][j], l[i][j + 1]) - dungeon[i][j]
                if l[i][j] <= 0:
                    l[i][j] = 1
        return l[0][0]


mySolution = Solution()
dungeon = [[0]]
re = mySolution.calculateMinimumHP(dungeon)
print(re)
