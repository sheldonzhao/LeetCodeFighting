'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k <= 1:
            return head
        dummy = ListNode(None)
        dummy.next = head
        self.last_kth_node = dummy
        count = 0
        node = {}
        while head:
            node[count] = head
            count += 1
            head = head.next
            if count == k:
                self.reverse(node, k)
                count = 0
        return dummy.next

    def reverse(self, node, k):
        temp = node[k - 1].next
        for i in range(k - 1):
            node[k - i - 1].next = node[k - i - 2]
        node[0].next = temp
        self.last_kth_node.next = node[k - 1]
        self.last_kth_node = node[0]

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
re = mySolution.reverseKGroup(head, 3)
mySolution.print(re)
