'''
Given a binary tree, find the left most element in the last row of the tree.
'''

from copy import deepcopy


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.path = []
        self.ans = []
        self.value = None

    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        if not root.left and not root.right:
            return root.val
        self.traversal(root)
        return self.value

    def traversal(self, root):
        if not root.left and not root.right:
            if len(self.path) > len(self.ans):
                self.ans = deepcopy(self.path)
                self.value = root.val
        if root.left:
            self.path.append(-1)
            self.traversal(root.left)
        if root.right:
            self.path.append(1)
            self.traversal(root.right)
        if len(self.path) >= 1:
            self.path.pop()


mySolution = Solution()
root = TreeNode(2)
root.left = TreeNode(None)
root.left.left = TreeNode(1)
# root.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.left.left = TreeNode(7)
re = mySolution.findLeftMostNode(root)
print(re)
