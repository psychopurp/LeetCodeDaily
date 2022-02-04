#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     # two-pointer
    #     # time complexity: O(n)
    #     # space complexity: O(1)

    #     dummy = ListNode(0)
    #     dummy.next = head
    #     slow = fast = dummy

    #     for i in range(n+1):
    #         fast = fast.next

    #     while fast:
    #         slow = slow.next
    #         fast = fast.next
    #     slow.next = slow.next.next
    #     return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # stack solution
        # time complexity: O(n)
        # space complexity: O(n)
        node = ListNode(0)
        node.next = head
        stack = [node]
        while head:
            stack.append(head)
            head = head.next

        while n:
            stack.pop()
            n -= 1

        stack[-1].next = stack[-1].next.next
        return stack[0].next

# @lc code=end
