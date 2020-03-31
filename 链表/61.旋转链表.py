#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        tmp = head
        n = 1
        while tmp.next:
            tmp = tmp.next
            n += 1
        tmp.next = head
        index = n - k % n
        tmmp = head
        for i in range(index):
            tmp = tmp.next
        head = tmp.next
        tmp.next = None
        return head


# @lc code=end
