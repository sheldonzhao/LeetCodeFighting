'''
Serialization is the process of converting a data structure or object into
a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same
or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary search tree can be serialized to a string
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''
'''
以下code不仅适用于BST,同时适用于BT（没有重复数的情况），有重复数的话search_index_in_order（）无法返回正确的index，结果悲剧。
思路是1.序列化部分进行先序和中序遍历，得到字符串。2.反序列化部分依据先序和中序遍历的结果还原树
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return
        # record result of in order traversal
        self.stack = []
        self.in_order_traversal(root)
        in_order_str = ''
        for i in self.stack:
            in_order_str += str(i)+','
        # record result of pre order traversal
        self.stack = []
        self.pre_order_traversal(root)
        pre_order_str = ''
        for i in self.stack:
            pre_order_str += str(i)+','
        return (pre_order_str + in_order_str).strip(',')

    def in_order_traversal(self, root):
        if root.left is not None:
            self.in_order_traversal(root.left)
        self.stack.append(root.val)
        if root.right is not None:
            self.in_order_traversal(root.right)

    def pre_order_traversal(self, root):
        if root is None:
            return
        self.stack.append(root.val)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data is None:
            return
        order_str = data.split(',')
        pre_order_str = order_str[0:len(order_str)//2]
        in_order_str = order_str[len(order_str)//2:]
        self.index = 0
        tNode = self.buildTree(pre_order_str, in_order_str, 0, len(pre_order_str) - 1)
        return tNode

    def buildTree(self, pre_order_str, in_order_str, start, end):
        if start > end:
            return None
        tNode = TreeNode((pre_order_str[self.index]))
        self.index += 1

        if start == end:
            return tNode

        pos = self.search_index_in_order(in_order_str, tNode.val)
        tNode.left = self.buildTree(pre_order_str, in_order_str, start, pos - 1)
        tNode.right = self.buildTree(pre_order_str, in_order_str, pos + 1, end)

        return tNode

    def search_index_in_order(self, in_order_str, val):
        for i in range(len(in_order_str)):
            if in_order_str[i] == val:
                return i

    def test(self, root):
        self.stack = []
        self.pre_order_traversal(root)
        print(self.stack)


mySolution = Codec()
root = TreeNode(6)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.left.left = TreeNode(8)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root_bug = TreeNode(3)
root_bug.left=TreeNode(2)
root_bug.right=TreeNode(4)
root_bug.left.left=TreeNode(3)
re1 = mySolution.serialize(root)
print(re1)
treeNode = mySolution.deserialize(re1)
mySolution.test(treeNode)
