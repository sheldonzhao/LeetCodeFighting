# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.value = []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.traversal(root)
        self.value.sort()
        min_value = self.value[1] - self.value[0]
        for i in range(len(self.value) - 1):
            min_value = min(min_value, self.value[i + 1] - self.value[i])
        return min_value

    def traversal(self, root):
        self.value.append(root.val)
        if root.left:
            self.traversal(root.left)
        if root.right:
            self.traversal(root.right)


mySolution = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
re = mySolution.getMinimumDifference(root)
print(re)
