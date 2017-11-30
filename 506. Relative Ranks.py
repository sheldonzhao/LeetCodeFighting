'''
Given scores of N athletes, find their relative ranks and the men with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
'''
'''
浅拷贝与深拷贝的问题
'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ans = []
        len_nums = len(nums)
        temp=[]
        for i in nums:
            temp.append(i)
        temp.sort()
        for i in nums:
            index = temp.index(i)
            value = len_nums - index
            if value == 1:
                ans.append('Gold Medal')
            elif value == 2:
                ans.append('Silver Medal')
            elif value == 3:
                ans.append('Bronze Medal')
            else:
                ans.append(str(value))
        return ans


mySolution = Solution()
nums = [5, 4, 3, 2, 1]
re = mySolution.findRelativeRanks(nums)
print(re)
