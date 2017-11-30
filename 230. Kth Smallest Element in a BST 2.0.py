# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.val = 0
        self.preoder_traversal(root, k)
        return self.val
    #  the result of pre order traversal is sorted array
    def preoder_traversal(self, root, k):
        if root.left is not None:
            self.preoder_traversal(root.left, k)
        self.count += 1
        if self.count == k:
            self.val = root.val
        if root.right is not None:
            self.preoder_traversal(root.right, k)


mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(7)
re = mySolution.kthSmallest(root, 5)
print(re)
