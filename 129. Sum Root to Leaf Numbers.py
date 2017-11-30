# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    path_sum = 0
    totalSum = 0

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.DFS(root)
        return self.totalSum

    def DFS(self, root):
        if root is None:
            return

        self.path_sum = self.path_sum * 10 + root.val
        if root.left is None and root.right is None:
            self.totalSum += self.path_sum

        else:
            self.DFS(root.left)
            self.DFS(root.right)

        self.path_sum //= 10


mySolution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
total_sum = mySolution.sumNumbers(root)
print(total_sum)
