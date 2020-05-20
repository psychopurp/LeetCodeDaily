#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = pre = ListNode(0)
        pre.next = head
        count = 0
        while head:
            count += 1
            if count == k:
                nxt = head.next
                pre.next, pre = self.reverseOne(pre.next, head)
                pre.next = head = nxt
                count = 0
            else:
                head = head.next
        return dummy.next

    # 返回反转后的头和尾
    def reverseOne(self, head, tail):
        pre = None
        cur = head
        while True:
            nxt = cur.next
            cur.next = pre
            pre = cur
            if pre == tail:
                break
            cur = nxt
        return pre, head


# @lc code=end
