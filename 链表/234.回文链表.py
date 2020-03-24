#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     # 利用O(n)空间复杂度实现
    #     stack = []
    #     while head:
    #         stack.append(head.val)
    #         head = head.next
    #     for i in range(len(stack)//2):
    #         if stack[i] != stack[len(stack)-1-i]:
    #             return False
    #     return True

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # 利用反转链表实现
        half_node = self.end_of_first_half(head)
        reversed_head_node = self.reverse_list(half_node.next)
        while reversed_head_node:
            if reversed_head_node.val != head.val:
                return False
            reversed_head_node = reversed_head_node.next
            head = head.next
        return True

    def end_of_first_half(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        pre = None
        current = head
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        return pre
# @lc code=end
