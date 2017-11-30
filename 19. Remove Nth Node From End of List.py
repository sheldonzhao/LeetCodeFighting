'''
Given a linked list, remove the nth node from the end of list and return its head.
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(None)
        dummy.next = head
        fisrstPointer, secondPointer = dummy, dummy
        count = 0
        while head:
            fisrstPointer = fisrstPointer.next
            count += 1
            head = head.next
            if count > n:
                # secondPointer point to (n-1)th node
                secondPointer = secondPointer.next

        # when finishing traversal
        secondPointer.next = secondPointer.next.next
        return dummy.next

    def print(self, head):
        while head:
            print(head.val)
            head = head.next


mySolution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# mySolution.print(head)
mySolution.removeNthFromEnd(head, 2)
mySolution.print(head)
