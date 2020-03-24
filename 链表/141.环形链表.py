#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     # 利用哈希的方法解决
    #     hash_set = set()
    #     while head:
    #         if head in hash_set:
    #             return True
    #         else:
    #             hash_set.add(head)
    #             head = head.next
    #     return False

    def hasCycle(self, head: ListNode) -> bool:
        # 利用双指针的方法解决
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# @lc code=end
