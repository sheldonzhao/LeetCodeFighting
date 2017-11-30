'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
'''
'''
wrong answer, but I do not know why!
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
        if root is None:
            return []

        queue = []
        queue.append(root)
        stack = []
        while len(queue):
            length = len(queue)  # the num of nodes in a layer
            temp = []
            # append nodes of the next layer
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            queue += temp
            # pop out the nodes of the former layer
            for i in range(length):
                node = queue.pop(0)
                stack.append(node.val)
            stack.append(-1)  # -1 is the sign to separate layers
        # get the rightmost node from every layer
        ans = []
        for i in range(len(stack)):
            if stack[i] == -1:
                ans.append(stack[i - 1])
        return ans


mySolution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
root.right = TreeNode(3)
root.left.right.right = TreeNode(5)
re = mySolution.rightSideView(root)
print(re)
