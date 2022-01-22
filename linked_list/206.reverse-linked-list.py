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

    def reverseList(self, head: ListNode) -> ListNode:
        # time complexity: O(n)
        # space complexity: O(n) (stack spcae for recursive calls)

        if not head or not head.next:
            return head

        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return cur


# @lc code=end
