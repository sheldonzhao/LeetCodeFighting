'''
Majority Voting Algorithm
follow up1：n/k
follow up2: array is sorted，进一步优化算法。既然不排序情况下是O(n)，排序情况下面试官肯定expect比O(n)复杂度低的算法。这点觉悟要有
solution: binary search for range O(k*logN) k is constant. 对n*1/k,n*2/k...n*(k-1)，n 这k处的值做binary search,
得到他的leftmost index和rightmost index
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for i in nums:
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = i, 1
            elif count2 == 0:
                candidate2, count2 = i, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [i for i in (candidate1, candidate2) if nums.count(i) > len(nums) // 3]

mySolution = Solution()
nums = [1,2]
re = mySolution.majorityElement(nums)
print(re)
