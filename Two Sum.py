class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return
        for i in range(len(nums)):
            d = target - nums[i]
            sub_nums = nums[:i] + nums[i + 1:]
            if d in sub_nums:
                return [i, sub_nums.index(d) + 1]


solution = Solution()
nums = [3, 3]
target = 6
res = solution.twoSum(nums, target)
print(res)
