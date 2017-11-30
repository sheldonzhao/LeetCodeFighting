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
        self.stack = []
        self.traversal(root)
        print(self.stack)
        self.stack.sort()
        return self.stack[k - 1]

    def traversal(self, root):
        if root is None:
            return
        self.stack.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)


mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(2)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(7)
re = mySolution.kthSmallest(root, 3)
print(re)
