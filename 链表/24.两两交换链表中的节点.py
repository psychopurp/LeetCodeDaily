#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     # 递归解法 时间复杂度O(N) 空间复杂度 O(N)
    #     if not head or not head.next:
    #         return head

    #     first, second = head, head.next
    #     first.next = second.next
    #     second.next = first

    #     first.next = self.swapPairs(first.next)
    #     return second

    def swapPairs(self, head: ListNode) -> ListNode:
        # 非递归解法 时间复杂度O(N) 空间复杂度O(1)
        # pre -> a -> b -> b->next 转换成 pre -> b -> a -> b->next
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next

            a.next, b.next, pre.next = b.next, a, b
            pre = a
        return dummy.next


# @lc code=end
