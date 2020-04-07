#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     table = set()

    #     while headA or headB:
    #         if headA:
    #             if headA in table:
    #                 return headA
    #             table.add(headA)
    #             headA = headA.next
    #         if headB:
    #             if headB in table:
    #                 return headB
    #             table.add(headB)
    #             headB = headB.next
    #     return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 空间复杂度O(1)

        tmpA = headA
        tmpB = headB
        while tmpA or tmpB:
            if tmpA == tmpB:
                return tmpA
            if tmpA:
                tmpA = tmpA.next
            else:
                tmpA = headB
            if tmpB:
                tmpB = tmpB.next
            else:
                tmpB = headA
        return None


# @lc code=end
