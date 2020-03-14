#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def generate(self, data):
#         head = ListNode(data[0])
#         temp = head

#         for i in data[1:]:
#             temp.next = ListNode(i)
#             temp = temp.next
#         return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)

        while l1 or l2 or carry:
            var1 = var2 = 0

            if l1:
                var1 = l1.val
                l1 = l1.next
            if l2:
                var2 = l2.val
                l2 = l2.next

            carry, val = divmod(var1+var2+carry, 10)

            n.next = ListNode(val)

            n = n.next

        return root.next


# @lc code=end
# def test(l1, l2):
#     temp = 0
#     flag = True
#     result = None
#     tNode = None

#     while flag:
#         var1, var2 = 0, 0
#         if (l1 is None) and (l2 is None):
#             break
#         if l1:
#             var1 = l1.val
#             l1 = l1.next
#         if l2:
#             var2 = l2.val
#             l2 = l2.next

#         val = (var1+var2+temp) % 10
#         temp = 0
#         if (var1+var2) >= 10:
#             temp = 1

#         if result is None:
#             result = ListNode(val)
#             tNode = result
#             continue

#         tNode.next = ListNode(val)

#         tNode = tNode.next

#     return result


# a = ListNode(0)
# d1 = a.generate([2, 4, 3])
# d2 = a.generate([5, 6, 4])
# test(d1, d2)
