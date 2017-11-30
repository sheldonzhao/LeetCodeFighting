'''
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        pointer = head.next
        # record last_odd_node for inserting the next odd node later
        last_odd_node = head
        while pointer.next:
            # next_node is the next even node
            next_node = pointer.next.next
            # insert odd node after the last_odd_node
            temp = last_odd_node.next
            last_odd_node.next = pointer.next
            pointer.next.next = temp
            # after insert, change last_odd_node
            last_odd_node = pointer.next
            # connect former even node to next even node
            pointer.next = next_node
            if pointer.next:
                # move point to next even node
                pointer = pointer.next
            else:
                # no node left
                break
        return head

    # for test
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
head.next.next.next.next.next = ListNode(6)
# mySolution.print(head)
mySolution.oddEvenList(head)
mySolution.print(head)
