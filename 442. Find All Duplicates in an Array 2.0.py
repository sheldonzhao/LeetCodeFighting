'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
'''
'''
better solution: use index
procedure:
1.traversal get number x and make nums[abs(x)-1] negative.
2.If x appears twice, traversal will find that negative num again.
'''


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                #  1 ≤ a[i] ≤ n (n = size of array)
                nums[abs(x) - 1] *= -1
        return res


mySolution = Solution()
nums = [1, 2, 30, 3, 4, 4]
re = mySolution.findDuplicates(nums)
print(re)
