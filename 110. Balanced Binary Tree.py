'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) \
               and self.isBalanced(root.right)

    def get_height(self, root):
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))


mySolution = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(3)
# root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
# root.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
re = mySolution.isBalanced(root)
print(re)
