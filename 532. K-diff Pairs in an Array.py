'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
'''
'''
result:TLE
mindset: 在能够确定值的情况下，不要用brute force， 直接hashmap
Time: O(n**2)
'''


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        len_nums = len(nums)
        l = []
        nums = sorted(nums)
        for i in range(len_nums):
            for j in range(i + 1, len_nums):
                if abs(nums[i] - nums[j]) == k:
                    if [nums[i], nums[j]] not in l and [nums[j], nums[i]] not in l:
                        l.append([nums[i], nums[j]])
                elif abs(nums[i] - nums[j]) > k:
                    break
        return len(l)


mySolution = Solution()
nums = [3, 1, 4, 1, 5]
k = 2
re = mySolution.findPairs(nums, k)
print(re)
