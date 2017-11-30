'''
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed factor gi,
which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj. If sj >= gi,
we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.
'''


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        if not g or not s: return 0
        g = sorted(g)
        s = sorted(s)
        res = 0
        index = 0
        for i in range(len(g)):
            child_size = g[i]
            for j in range(index, len(s)):
                if child_size <= s[j]:
                    res += 1
                    s.pop(j)
                    break
            index = j
        return res


mySolution = Solution()
g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
re = mySolution.findContentChildren(g, s)
print(re)
