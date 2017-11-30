'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
'''


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        hash_map = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                if i - hash_map[nums[i]] <= k:
                    return True
                hash_map[nums[i]] = i
        return False


mySolution = Solution()
nums = [1, 2, 1, 4, 1, 5, 6]
k = 2
re = mySolution.containsNearbyDuplicate(nums, k)
print(re)
