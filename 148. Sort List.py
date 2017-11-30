'''
Sort a linked list in O(n log n) time using constant space complexity.
'''
'''
只完成了功能，并不符合时间和空间的O(n)
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
        #  create list to save value of head
        lst = [head.val]
        while head.next:
            head = head.next
            lst.append(head.val)
        #  sort
        lst.sort()
        #  create ListNode according to sorted list
        node = ListNode(lst.pop(0))
        save_node = node
        while lst:
            node.next = ListNode(lst.pop(0))
            node = node.next
        return save_node
