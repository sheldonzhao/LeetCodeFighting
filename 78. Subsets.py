'''
Given a set of distinct integers, nums, return all possible subsets.
'''


class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)


mySolution = Solution()
nums = [1, 2, 3, 4]
re = mySolution.subsets(nums)
print(re)
