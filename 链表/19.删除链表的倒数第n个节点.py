#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     应用数组实现 时间复杂度O(n),空间复杂度O(n)
    #     tmp = head
    #     node_list = []
    #     while tmp:
    #         node_list.append(tmp)
    #         tmp = tmp.next

    #     node = node_list[-n]
    #     if node == node_list[0]:
    #         result = node.next
    #         node = None
    #         return result
    #     elif node == node_list[-1]:
    #         node_list[-2].next = None
    #         return node_list[0]
    #     else:
    #         node = None
    #         pre = node_list[-n-1]
    #         pre.next = node_list[-n+1]
    #         return node_list[0]

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 双指针实现 时间复杂度O(n) 空间复杂度o(1)
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        q = dummy
        for i in range(n+1):
            q = q.next
        while q:
            q = q.next
            p = p.next
        p.next = p.next.next

        return dummy.next

# @lc code=end
