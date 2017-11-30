'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        pointer1, pointer2 = head, head
        while pointer1 and pointer2:
            pointer1 = pointer1.next
            if pointer2.next == None:
                return False
            pointer2 = pointer2.next.next
            if pointer1 == pointer2:
                return True
        return False


head = ListNode(1)
s = Solution()
res = s.hasCycle(head)
print(res)
