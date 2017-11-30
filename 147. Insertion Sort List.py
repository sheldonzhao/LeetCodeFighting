'''
Sort a linked list using insertion sort.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        first_node = ListNode(-1)

        while head:
            node = first_node
            while node.next and head.val > node.next.val:
                node = node.next
            next_head = head.next
            head.next = node.next
            node.next = head
            head = next_head

        return first_node.next

    def print(self, head):
        while head:
            print(head.val)
            head = head.next


mySolution = Solution()
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(5)
# head.next.next.next = ListNode(3)
re=mySolution.insertionSortList(head)
mySolution.print(re)
