'''
Given a binary tree, find its minimum depth.

The minmum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.
'''
'''
1.simple: solution like leetcode 111, recursion
2.more efficient: non-recursion
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

    # BFS T:O(n)
    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [root]
        count_level = 0
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            count_level += 1
        return count_level

    # DFS
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


mySolution = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
re = mySolution.maxDepth(root)
print(re)
