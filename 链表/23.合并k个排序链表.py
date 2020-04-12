#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        def merge_2_list(l1, l2):
            head = ListNode(0)
            tmp = head
            if not l2:
                return l1
            while l1 and l2:
                if l1.val <= l2.val:
                    tmp.next = l1
                    l1 = l1.next
                else:
                    tmp.next = l2
                    l2 = l2.next
                tmp = tmp.next
            if l1:
                tmp.next = l1
            elif l2:
                tmp.next = l2
            return head.next

        while len(lists) != 1:
            tmp = []
            n = len(lists)
            for i in range(0, n, 2):
                l1 = lists.pop(0)
                l2 = None if len(lists) == 0 else lists.pop(0)
                tmp.append(merge_2_list(l1, l2))
            if len(tmp) == 1:
                return tmp[0]
            lists = tmp

# @lc code=end
