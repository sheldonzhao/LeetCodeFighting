class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if not findNums:
            return []

        ans = []
        for i in findNums:
            flag=0
            index = nums.index(i)
            for j in range(index, len(nums)):
                if nums[j] > i:
                    ans.append(nums[j])
                    flag=1
                    break
            if flag==0:
                ans.append(-1)

        return ans


mySolution = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
re = mySolution.nextGreaterElement(nums1, nums2)
print(re)
