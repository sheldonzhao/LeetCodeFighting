'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root.
" Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        self.DFS(root, sum)
        if root.left:
            self.pathSum(root.left, sum)
        if root.right:
            self.pathSum(root.right, sum)
        return self.count

    def DFS(self, root, sum):
        if root.val == sum:
            self.count += 1
        if root.left:
            self.DFS(root.left, sum - root.val)
        if root.right:
            self.DFS(root.right, sum - root.val)




mySolution = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(8)
# root.left.right = TreeNode(4)
# root.left.right.left = TreeNode(3)
# root.left.right.right = TreeNode(5)
re = mySolution.pathSum(root, 8)
print(re)
