#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     # two pointer iteration
    #     # time complexity: O(n)
    #     # spcae complexity: O(1)
    #     prev = None
    #     cur = head

    #     while cur:
    #         nextNode = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = nextNode

    #     return prev

    # def reverseList(self, head: ListNode) -> ListNode:
    #     # time complexity: O(n)
    #     # space complexity: O(n) (stack spcae for recursive calls)

    #     if not head or not head.next:
    #         return head

    #     cur = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None

    #     return cur

    def reverseList(self, head: ListNode) -> ListNode:
        # recursion solution 2
        # time complexity: O(n)
        # space complexity: O(n) (stack spcae for recursive calls)

        # return new head and tail
        def reverse(node):
            if not node.next:
                return node, node

            head, tail = reverse(node.next)
            tail.next = node
            node.next = None
            return head, node

        if not head:
            return None

        new_head, tail = reverse(head)
        return new_head


# @lc code=end
