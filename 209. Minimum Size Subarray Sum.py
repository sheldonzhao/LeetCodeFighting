'''
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''
'''
LTE
learning point: index = min(ans, key=ans.get) return key which ans[key] has min value.
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            if i >= s:
                return 1

        len_nums = len(nums)
        ans = {}
        for i in range(len_nums):
            count = 0
            count_num = 0
            while count < s and i + count_num < len_nums:
                count += nums[i + count_num]
                count_num += 1
                if count >= s:
                    ans[i] = count_num
        if not ans:
            return 0
        index = min(ans, key=ans.get)
        return ans[index]


mySolution = Solution()
nums = [2, 3, 1, 2, 4, 3]
s = 7
re = mySolution.minSubArrayLen(s, nums)
print(re)
