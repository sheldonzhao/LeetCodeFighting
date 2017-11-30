'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    record = []

    # fail -> pre-order traversal
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.traversal(root)
        print(self.record)
        l = self.record[:len(self.record) // 2]
        if len(self.record) % 2 == 0:
            r = self.record[len(self.record) // 2:]
        else:
            r = self.record[len(self.record) // 2 + 1:]

        return l == r[::-1]

    def traversal(self, root):
        if not root:
            return
        if root.left:
            self.traversal(root.left)
        self.record.append(root.val)
        if root.right:
            self.traversal(root.right)

    flag = 0
    def isSymmetric2(self, root):
        if not root:
            return True
        self.helper(root.left, root.right)
        return self.flag == 0

    def helper(self, left, right):
        if not left and not right:
            return
        if left == None or right == None:
            self.flag = 1
            return
        elif left.val != right.val:
            self.flag = 1
        self.helper(left.left, right.right)
        self.helper(left.right, right.left)



    def isSymmetric3(self, root):
        if not root:
            return True
        return  self.helper3(root.left, root.right)


    def helper3(self, left, right):
        if not left and not right:
            return True
        if left == None or right == None:
            return False
        elif left.val != right.val:
            return False
        return self.helper3(left.left, right.right) and self.helper3(left.right, right.left)

