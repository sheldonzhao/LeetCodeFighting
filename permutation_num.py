class solution():
    def permute(self, nums):

        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


nums = [1, 2, 3]
s=solution()
r=s.permute(nums)

print(r)