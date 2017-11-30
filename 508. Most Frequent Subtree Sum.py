# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.ans = []
        self.sum = 0
        self.traversal(root)
        record = {}
        for i in self.ans:
            if i in record:
                record[i] += 1
            else:
                record[i] = 1

        max_num = max(record.values())
        res = []
        for key, value in record.items():
            if value == max_num:
                res.append(key)
        return res

    def traversal(self, root):
        if not root.left and not root.right:
            self.ans.append(root.val)
        else:
            self.sum = 0
            self.add_sub_tree(root)
            self.ans.append(self.sum)
        if root.left:
            self.traversal(root.left)
        if root.right:
            self.traversal(root.right)

    def add_sub_tree(self, root):
        if not root:
            return
        self.sum += root.val
        if root.left:
            self.add_sub_tree(root.left)
        if root.right:
            self.add_sub_tree(root.right)


mySolution = Solution()
root = TreeNode(5)
root.left = TreeNode(-5)
root.right = TreeNode(2)
re = mySolution.findFrequentTreeSum(root)
print(re)
