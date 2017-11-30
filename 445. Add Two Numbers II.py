'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return ListNode(None)
        # get number from tree
        num1, num2 = 0, 0
        if l1:
            num1 = self.getNumber(l1)
        if l2:
            num2 = self.getNumber(l2)
        sum_value = num1 + num2
        # rebuild tree
        dummy = ListNode(None)
        temp = dummy
        for i in str(sum_value):
            dummy.next = ListNode(int(i))
            dummy = dummy.next
        return temp.next

    def getNumber(self, head):
        num = 0
        while head:
            num = 10 * num + head.val
            head = head.next
        return num

    def print(self, head):
        while head:
            print(head.val)
            head = head.next


mySolution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l2 = ListNode(2)
l2.next = ListNode(3)
re = mySolution.addTwoNumbers(l1, l2)
mySolution.print(re)