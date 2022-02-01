#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     # recursion solution
    #     # time complexity: O(n*k)
    #     # space complexity: O(n) stack space used for recursion

    #     cur = head
    #     count = 0
    #     while cur and count != k:
    #         count += 1
    #         cur = cur.next

    #     # if count=k then reverse the list
    #     if count == k:
    #         # cur equals to next head of sub list
    #         node = self.reverseKGroup(cur, k)
    #         while count:
    #             tmp = head.next
    #             head.next = node
    #             node = head
    #             head = tmp
    #             count -= 1
    #         head = node

    #     return head

    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     # time complexity: O(n*k)
    #     # space complexity: O(1)
    #     def reverse(head: ListNode, tail: ListNode):
    #         prev = None
    #         cur = head
    #         while True:
    #             nextHead = cur.next
    #             cur.next = prev
    #             prev = cur
    #             if prev == tail:
    #                 break
    #             cur = nextHead

    #         return tail, head

    #     dummy = prev = ListNode(0)
    #     prev.next = head
    #     count = 0
    #     while head:
    #         count += 1
    #         if count == k:
    #             nextNode = head.next
    #             newHead, newTail = reverse(prev.next, head)
    #             prev.next, prev = newHead, newTail
    #             prev.next = head = nextNode
    #             count = 0
    #         else:
    #             head = head.next
    #     return dummy.next

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # stack solution
        # time complexity: O(n*k)
        # space complexity: O(k)
        dummy = prev = ListNode(0)
        prev.next = head

        while True:
            stack = []
            cur = head
            # load node
            while cur:
                stack.append(cur)
                cur = cur.next
                if stack and len(stack) == k:
                    break

            if len(stack) == k:
                # reverse
                while stack:
                    prev.next = stack.pop()
                    prev = prev.next
                prev.next = head = cur
            else:
                stack.clear()
                prev.next = head
                break

        return dummy.next

    # @lc code=end
