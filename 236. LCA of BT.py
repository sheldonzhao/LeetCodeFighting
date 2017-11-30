'''
Given a binary tree (BT),
find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node
 in T that has both v and w as descendants
 (where we allow a node to be a descendant of itself).”
'''
'''
递归求解普通的二叉树的LCA：
1. 分别求出 left 分支 的LCA 和 right 分支的LCA
2. 然后比较 LCA(left) 和 LCA(right) 的值
    a. 如果 LCA(left) 为空，那么返回 LCA(right)
    b. 如果 LCA(right) 为空， 那么返回 LCA(left)
    c. 如果 LCA(left) 和 LCA(right) 都不为空，那么返回跟节点
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
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root.val

        tree_left = self.lowestCommonAncestor(root.left, p, q)
        tree_right = self.lowestCommonAncestor(root.right, p, q)

        if tree_left is not None and tree_right is not None:
            return root.val
        if tree_left is not None:
            return tree_left
        if tree_right is not None:
            return tree_right
        return None


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
re = mySolution.lowestCommonAncestor(root, p, q)
print(re)
