'''
Given a binary tree (BT),
find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes v and w as the lowest node
 in T that has both v and w as descendants
 (where we allow a node to be a descendant of itself).”
'''
'''
wrong answer
问题出在给了两个重复的数-100，-100.我的算法找到了第一个-100和第二个数的LCA,
而题目给的解是第二个-100和第二个数的LCA。算法在其他情况下正确。
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
        self.stack = []
        self.flag = 0
        self.recordPath(p, root)
        stack1 = self.stack[0:self.stack.index(p.val) + 1]
        self.stack = []
        self.flag = 0
        self.recordPath(q, root)
        stack2 = self.stack[0:self.stack.index(q.val) + 1]

        print(stack1)
        print(stack2)
        length = min(len(stack1), len(stack2))
        for i in range(length):
            if stack1[i] != stack2[i]:
                return stack1[i - 1]
            else:
                val = stack1[i]
        return val

    def recordPath(self, node, root):
        # use stack to save path
        self.stack.append(root.val)

        if node.val == root.val:
            self.flag = 1
            return
        if root.left is not None:
            self.recordPath(node, root.left)
        if root.right is not None:
            self.recordPath(node, root.right)

        if self.flag == 0:
            self.stack.pop()


mySolution = Solution()
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(2)
root.left.right.right = TreeNode(5)
p = TreeNode(2)
q = TreeNode(5)
re = mySolution.lowestCommonAncestor(root, p, q)
print(re)
