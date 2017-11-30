'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        for i in hashMap.keys():
            if hashMap[i] == 1:
                return i

    def singleNumber2(self, nums):
        # A ^ A = 0 and A ^ B ^ A = B
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
            print(res)
        return res


s = Solution()
nums = [1, 2, 2, 3, 3]
res = s.singleNumber2(nums)
print(res)
