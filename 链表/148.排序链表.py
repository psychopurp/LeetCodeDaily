#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 归并排序合并

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow.next
        # 切割
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        while left:
            h.next = left
            h = h.next
            left = left.next
        while right:
            h.next = right
            h = h.next
            right = right.next
        return res.next

# @lc code=end
