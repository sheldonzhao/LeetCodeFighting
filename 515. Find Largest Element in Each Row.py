'''
You need to find the largest value in each row of a binary tree.
'''
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findValueMostElement(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = []
        queue.append(root)
        ans = []
        while len(queue) > 0:
            len_queue = len(queue)
            temp = deepcopy(queue)
            for node in temp:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            nums = []
            for i in range(len_queue):
                node = queue.pop(0)
                if node.val or node.val == 0:
                    nums.append(node.val)
            ans.append(max(nums))
        return ans


mySolution = Solution()
root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(None)
root.right.right = TreeNode(9)
re = mySolution.findValueMostElement(root)
print(re)
