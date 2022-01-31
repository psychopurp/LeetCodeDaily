#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointer solution
        # time complexity: O(n)
        # space complexity: O(1)

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        pass

# @lc code=end
