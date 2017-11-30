'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #  validate the argument
        if not root:
            return []
        queue, ans = [root], []
        while queue:
            node_every_layer = len(queue)
            while node_every_layer:
                right_most = queue.pop(0)
                if right_most.left:
                    queue.append(right_most.left)
                if right_most.right:
                    queue.append(right_most.right)
                node_every_layer -= 1
            ans.append(right_most.val)
        return ans

mySolution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
#root.left.left.left = TreeNode(8)
#root.left.right = TreeNode(4)
root.right = TreeNode(3)
#root.left.right.right = TreeNode(5)
re = mySolution.rightSideView(root)
print(re)
