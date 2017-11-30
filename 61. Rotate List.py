'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        hash_map = {}
        index = 0
        head_copy = head
        while head:
            hash_map[index] = head
            index += 1
            head = head.next
        k = k % index
        if index == k or k == 0:
            return head_copy
        hash_map[index - k - 1].next = None
        hash_map[index - 1].next = head_copy
        return hash_map[index - k]

    def print(self, head):
        while head:
            print(head.val)
            head = head.next


mySolution = Solution()
head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
re = mySolution.rotateRight(head, 99)
mySolution.print(re)
