#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#


# @lc code=start
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.move_node_to_tail(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.move_node_to_tail(node)
        else:
            node = Node(key, value)
            while len(self.hashmap) >= self.capacity:
                self.remove_oldest_node()
            self.hashmap[node.key] = node

            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node

    def move_node_to_tail(self, node: Node):

        # 先将Node 拎出来
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def remove_oldest_node(self):
        oldest_node = self.head.next
        self.hashmap.pop(oldest_node.key)
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
