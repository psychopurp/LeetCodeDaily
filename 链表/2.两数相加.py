#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)
        tmp = head

        index = 0
        while l1 or l2:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            val = (val1 + val2 + index) % 10
            index = (val1 + val2 + index) // 10
            tmp.next = ListNode(val)
            tmp = tmp.next
        if index != 0:
            tmp.next = ListNode(1)
            tmp = tmp.next
        return head.next


# @lc code=end
