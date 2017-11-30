'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
'''
time: O(n!)
mindset: DFS, put every number to the first position
'''


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        if len(nums) == 1: return [nums]
        res = []
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                for j in self.permuteUnique(nums[:i] + nums[i + 1:]):
                    res.append([nums[i]] + j)
        return res


mySolution = Solution()
nums = [1, 1, 3, 4]
re = mySolution.permuteUnique(nums)
print(re)
print(len(re))
