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
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.hash_map = {}
        return self.robDFS(root)

    def robDFS(self, root):
        if not root:
            return 0
        if root in self.hash_map:
            return self.hash_map[root]
        ans = 0
        if root.left:
            ans += self.robDFS(root.left.left) + self.robDFS(root.left.right)
        if root.right:
            ans += self.robDFS(root.right.left) + self.robDFS(root.right.right)
        ans = max(ans + root.val, self.robDFS(root.left) + self.robDFS(root.right))
        self.hash_map[root] = ans
        return ans
