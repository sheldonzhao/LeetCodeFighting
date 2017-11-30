'''
Reverse a singly linked list.
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # iterately
        # TODO: unknown inf loop in while
        if not head:
            return None
        curr = None
        while head:
            curr = head.next
            curr.next = head
            print(curr.next.val)
            head = head.next
        return curr

    def reverseList2(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    def reverseList3(self, head):
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)


n1 = ListNode(1)
n1.next = ListNode(2)
#n1.next.next = ListNode(3)
s = Solution()
res = s.reverseList(n1)
print(res)
