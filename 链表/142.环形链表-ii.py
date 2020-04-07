#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     # 时间复杂度O(N),空间复杂度O(N)
    #     visited = set()
    #     while head:
    #         if head in visited:
    #             return head
    #         else:
    #             visited.add(head)
    #             head = head.next
    #     return head

    def detectCycle(self, head: ListNode) -> ListNode:
        # 时间复杂度O(N),空间复杂度O(1)
        slow, fast = head, head
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if flag:
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast
        else:
            return None


# @lc code=end
