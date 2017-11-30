'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to
the original key plus sum of all keys greater than the original key in BST.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.sum = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        self.DFS(root)
        return root

    def DFS(self, root):
        if not root: return
        self.DFS(root.right)
        t = root.val
        root.val += self.sum
        self.sum += t
        self.DFS(root.left)


mySolution = Solution()
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
re = mySolution.convertBST(root)
