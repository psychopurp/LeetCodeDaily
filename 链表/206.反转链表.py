#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     # 双指针迭代
    #     current = head
    #     pre = None
    #     while current:
    #         next = current.next
    #         current.next = pre
    #         pre = current
    #         current = next
    #     return pre

    def reverseList(self, head: ListNode) -> ListNode:
        # 递归
        if not head or not head.next:
            return head

        curr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return curr

# @lc code=end
