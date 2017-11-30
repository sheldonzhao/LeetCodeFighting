class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        dict_nums = {}
        for i in range(len_nums):
            dict_nums[nums[i]] = i

        for i in range(len_nums):
            if target - nums[i] in dict_nums:
                if dict_nums[target - nums[i]] != i:
                    return [dict_nums[target - nums[i]], i]


mySolution = Solution()
nums = [3, 2, 4]
target = 6
re = mySolution.twoSum(nums, target)
print(re)
