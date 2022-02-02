#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     # time complexity: O(n)
    #     # space complexity: O(m+n) : new linked list node

    #     dummy = head = ListNode(0)

    #     while list1 or list2:
    #         if list1 and list2:
    #             if list1.val < list2.val:
    #                 val = list1.val
    #                 list1 = list1.next
    #             else:
    #                 val = list2.val
    #                 list2 = list2.next
    #         elif list1:
    #             val = list1.val
    #             list1 = list1.next
    #         else:
    #             val = list2.val
    #             list2 = list2.next
    #         dummy.next = ListNode(val)
    #         dummy = dummy.next
    #     return head.next

    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     # time complexity: O(n)
    #     # space complexity: O(1)
    #     head = cur = ListNode(0)

    #     while list1 and list2:
    #         if list2.val < list1.val:
    #             cur.next = list2
    #             list2 = list2.next
    #         else:
    #             cur.next = list1
    #             list1 = list1.next
    #         cur = cur.next

    #     cur.next = list1 or list2
    #     return head.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # recursion solution
        # time complexity: O(n)
        # space complexity: O(n) : stack used in recursion
        if not list1:
            return list2
        if not list2:
            return list1

        if list2.val < list1.val:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1


# @lc code=end
