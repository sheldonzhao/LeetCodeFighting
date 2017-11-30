'''
Given a binary search tree (BST),
find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node
 in T that has both v and w as descendants
 (where we allow a node to be a descendant of itself).”
 BST的暴力法特别简单，使用递归的思路求解：
1， 如果 当前节点(从root开始) 的值大于p, q的值，那么公共祖先一定在树的左分支
2， 如果 当前节点的值小于p, q节点的值，那么公共祖先一定在树的右分支
3， 如果当前节点的值大于p(或者q), 小于q(或者p), 那么该节点就是目标节点
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
        if root.val is None:
            return
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return root.val


mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = TreeNode(5)
q = TreeNode(4)
re = mySolution.lowestCommonAncestor(root, p, q)
print(re)
