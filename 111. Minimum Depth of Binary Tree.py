'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.record = []
        self.count = 0

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.traversal(root)
        print(self.record)
        return min(self.record)

    def traversal(self, root):
        self.count += 1
        if not root.left and not root.right:
            self.record.append(self.count)
        if root.left:
            self.traversal(root.left)
        if root.right:
            self.traversal(root.right)
        self.count -= 1


mySolution = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
#root.left.right.left = TreeNode(3)
#root.left.right.right = TreeNode(5)
re = mySolution.minDepth(root)
print(re)
