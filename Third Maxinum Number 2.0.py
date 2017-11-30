'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  array to store top3 max numbers
        array = []
        for i in nums:
            if i not in array:
                array.append(i)
            if len(array) == 3:
                break
        # special case
        if len(array) < 3:
            return max(array)

        # normal case
        array.sort()
        length = len(nums)
        for i in range(3, length):
            if nums[i] < array[0]:
                continue
            # array[0]<num[i]<array[1]
            elif nums[i] > array[0] and nums[i] < array[1]:
                array[0] = nums[i]
            # array[1]<num[i]<array[2]
            elif nums[i] > array[1] and nums[i] < array[2]:
                array[0] = array[1]
                array[1] = nums[i]
            # array[2]<num[i]
            elif nums[i] > array[2]:
                array[0] = array[1]
                array[1] = array[2]
                array[2] = nums[i]

        return array[0]


solution = Solution()
num1 = [3, 2, 1]
num2 = [1, 2]
num3 = [2, 2, 3, 1]
num4 = [2, 2, 2, 1]
num5 = [1, 2, 2, 5, 3, 5]

print(solution.thirdMax(num5))
