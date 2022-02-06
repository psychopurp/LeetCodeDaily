#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reorderList(self, head: ListNode) -> None:
    #     # using stack to store reversed nodes
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = []
    #     slow = fast = head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next

    #     cur = slow
    #     while cur:
    #         stack.append(cur)
    #         cur = cur.next

    #     cur = head
    #     while stack:
    #         node = stack.pop()
    #         node.next = cur.next
    #         cur.next = node
    #         cur = cur.next.next
    #     slow.next = None

    def reorderList(self, head: ListNode) -> None:
        # time complexity: O(n)
        # space complexity: O(1)

        def reverseNode(node: ListNode) -> ListNode:
            prev = None
            cur = node
            while cur:
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode
            return prev

        # step 1: find middle
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        nextHead = slow.next
        # cut down the first half
        slow.next = None

        l1 = head
        # step 2: reverse second half
        l2 = reverseNode(nextHead)

        # step 3: merge lists
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l2 = l2_next
            l1 = l1_next

    # @lc code=end
