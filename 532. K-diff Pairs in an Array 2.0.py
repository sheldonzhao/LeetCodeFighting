'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
'''
'''
mindset: 在能够确定值的情况下，不要用brute force， 直接hash_map
Time: O(n)
'''


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = []
        if k < 0: return 0
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        count = 0
        unique_nums = set(nums)
        if k == 0:
            for i in unique_nums:
                if hash_map[i] > 1:
                    count += 1
        else:
            for i in unique_nums:
                if i + k in hash_map:
                    count += 1
        return count


mySolution = Solution()
nums = [3, 1, 4, 1, 5]
nums1 = [1, 3, 1, 5, 4]
k = 2
k1 = 0
re = mySolution.findPairs(nums, k)
print(re)
