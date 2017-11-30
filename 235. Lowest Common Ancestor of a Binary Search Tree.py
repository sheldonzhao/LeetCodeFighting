'''
Given a binary search tree (BST),
find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node
 in T that has both v and w as descendants
 (where we allow a node to be a descendant of itself).”
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.record = []
        self.value = []
        self.recordPath(p, root)
        re1 = self.record
        self.record = []
        self.recordPath(q, root)
        re2 = self.record

        if len(re1) <= len(re2):
            length = len(re1)
        else:
            length = len(re2)
        num = 0
        for i in range(length):
            if re1[i] == re2[i]:
                num += 1
            else:
                break
        print(self.value)
        return self.value[num]

    def recordPath(self, node, root):
        self.value.append(root.val)
        if node.val == root.val:
            return
        elif node.val < root.val:
            self.record.append(-1)
            self.recordPath(node, root.left)
        elif node.val > root.val:
            self.record.append(1)
            self.recordPath(node, root.right)


mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(4)
re = mySolution.lowestCommonAncestor(root, p, q)
print(re)
