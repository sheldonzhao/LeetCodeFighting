'''
Find the sum of all left leaves in a given binary tree.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.flag = 0
        self.sum = 0
        self.traversal(root)
        return self.sum

    def traversal(self, root):
        if self.flag == 1 and root.left is None and root.right is None:
            self.sum += root.val
        if root.left is not None:
            self.flag = 1
            self.traversal(root.left)
        self.flag = 0
        if root.right is not None:
            self.traversal(root.right)


mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
re = mySolution.sumOfLeftLeaves(root)
print(re)
