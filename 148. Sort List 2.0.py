'''
Sort a linked list in O(n log n) time using constant space complexity.
'''
'''
merge sort
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #  validate argument
        if not head or not head.next:
            return head


