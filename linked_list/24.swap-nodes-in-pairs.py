#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     # 递归解法 时间复杂度O(N) 空间复杂度 O(N)
    #     if not head or not head.next:
    #         return head

    #     first, second = head, head.next
    #     first.next = second.next
    #     second.next = first

    #     first.next = self.swapPairs(first.next)
    #     return second

    # def swapPairs(self, head: ListNode) -> ListNode:
    #     # 非递归解法 时间复杂度O(N) 空间复杂度O(1)
    #     # pre -> a -> b -> b->next 转换成 pre -> b -> a -> b->next
    #     dummy = pre = ListNode(0)
    #     pre.next = head
    #     while pre.next and pre.next.next:
    #         a = pre.next
    #         b = a.next

    #         a.next, b.next, pre.next = b.next, a, b
    #         pre = a
    #     return dummy.next

    # def swapPairs(self, head: ListNode) -> ListNode:
    #     # time complexity: O(n)
    #     # space complexity: O(1)

    #     def reverseNode(head: ListNode, tail: ListNode) -> ListNode:
    #         '''
    #         head->a->tail->d
    #         reverse it to head->tail->a->d
    #         return d
    #         '''
    #         head.next.next, tail.next, head.next = tail.next, head.next, tail

    #         return head.next.next

    #     dummy = pre = ListNode(0)
    #     dummy.next = head

    #     while pre and pre.next and pre.next.next:
    #         node = reverseNode(pre, pre.next.next)
    #         pre = node

    #     return dummy.next

    def swapPairs(self, head: ListNode) -> ListNode:
        # recursiion solution
        # time complexity: O(n)
        # spcae complexity: O(n)
        if not head or not head.next:
            return head

        newHead = head.next
        head.next.next, head.next = head, self.swapPairs(head.next.next)
        return newHead

# @lc code=end
