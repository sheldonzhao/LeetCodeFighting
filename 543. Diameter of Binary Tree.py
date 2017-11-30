'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
'''
'''
time: O(2**n)
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.DFS(root)
        return self.res

    def DFS(self, root):
        if not root: return -1
        l = self.DFS(root.left) + 1
        r = self.DFS(root.right) + 1
        self.res = max(self.res, l + r)
        return max(l, r)


mySolution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
re = mySolution.diameterOfBinaryTree(root)
print(re)
