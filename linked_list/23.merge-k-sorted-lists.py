#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.

from typing import List


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     # K-pointer, K represents the length of lists, N means node count
    #     # time complexity: O(K*N)
    #     # space complexity: O(1)
    #     dummy = head = ListNode(0)
    #     while True:
    #         idx = -1
    #         for i in range(len(lists)):
    #             if not lists[i]:
    #                 continue
    #             if idx == -1 or lists[i].val < lists[idx].val:
    #                 idx = i

    #         if idx == -1:
    #             break
    #         dummy.next = lists[idx]
    #         dummy = dummy.next
    #         lists[idx] = lists[idx].next

    #     return head.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     # min heap solution
    #     # time complexity: O(N*logK)
    #     # space complexity: O(K)

    #     import heapq
    #     dummy = head = ListNode(0)
    #     minHeap = []

    #     for i in range(len(lists)):
    #         if lists[i]:
    #             heapq.heappush(minHeap, (lists[i].val, i, lists[i]))

    #     while minHeap:
    #         _, i, node = heapq.heappop(minHeap)
    #         dummy.next = node
    #         dummy = dummy.next
    #         if node.next:
    #             heapq.heappush(minHeap, (node.next.val, i, node.next))

    #     return head.next

    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     # divide and conquer
    #     # time complexity: O(N*logK)
    #     # space complexity: O(logk) stack space for recursion

    #     def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
    #         # time complexity: O(2*N/K)
    #         dummy = head = ListNode(0)

    #         while l1 and l2:
    #             if l1.val < l2.val:
    #                 dummy.next = l1
    #                 l1 = l1.next
    #             else:
    #                 dummy.next = l2
    #                 l2 = l2.next
    #             dummy = dummy.next

    #         dummy.next = l1 or l2

    #         return head.next

    #     def merge(lists, left: int, right: int) -> ListNode:
    #         # devide time complexity: O(logK)
    #         if left == right:
    #             return lists[left]
    #         mid = (left+right)//2
    #         l1 = merge(lists, left, mid)
    #         l2 = merge(lists, mid+1, right)
    #         return merge2Lists(l1, l2)

    #     if not lists:
    #         return None
    #     return merge(lists, 0, len(lists)-1)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 0,1 2,3 4,5 6,7 8
        # 0,2 4,6 8
        # 0,4 ,8
        # 0,8

        # divide and conquer: iterating
        # time complexity: O(N*logK) => O(logK * K * 2N/K)
        # space complexity: O(1)

        def merge2Lists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = head = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            dummy.next = l1 or l2
            return head.next

        if not lists:
            return None

        nonce = 1
        n = len(lists)
        while n:
            i = 0
            while i+nonce < len(lists):
                lists[i] = merge2Lists(lists[i], lists[i+nonce])
                i += 2*nonce
            nonce *= 2
            n = n // 2
        return lists[0]


# @lc code=end
