'''
Given a binary tree, find the left most element in the last row of the tree.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeftMostNode(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return

        queue = []
        queue.append(root)
        left_most = []
        while len(queue) > 0:
            len_queue = len(queue)
            flag = 0
            for node in queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len_queue):
                node = queue.pop(0)
                if not flag:
                    left_most.append(node)
                    flag = 1
        return left_most.pop().val


mySolution = Solution()
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
re = mySolution.findLeftMostNode(root)
print(re)
