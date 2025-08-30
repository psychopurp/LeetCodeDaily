#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from typing import Dict, Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.val = value
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    """
    solution 1 : implement double-ended linked list
    """

    # class CacheItem:
    #     def __init__(self, key: int, val: int) -> None:
    #         self.key = key
    #         self.val = val
    #         self.prev: Optional[LRUCache.CacheItem] = None
    #         self.next: Optional[LRUCache.CacheItem] = None

    # def __init__(self, capacity: int):
    #     self.cache: Dict[int, LRUCache.CacheItem] = {}
    #     self.capacity = capacity
    #     self.head: LRUCache.CacheItem = LRUCache.CacheItem(0, 0)
    #     self.tail: LRUCache.CacheItem = LRUCache.CacheItem(0, 0)

    #     self.head.next = self.tail
    #     self.tail.prev = self.head

    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1

    #     item = self.cache[key]
    #     self.move_node_to_head(item)
    #     return item.val

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         node = self.cache[key]
    #         node.val = value
    #         self.move_node_to_head(node)
    #         return

    #     if len(self.cache) == self.capacity:
    #         self.evict(self.tail.prev)

    #     item = LRUCache.CacheItem(key, value)
    #     self.cache[key] = item
    #     self.move_node_to_head(item)

    # def evict(self, cache_item: CacheItem):
    #     self.take_node_out(cache_item)
    #     self.cache.pop(cache_item.key)

    # def take_node_out(self, cache_item: CacheItem):
    #     if cache_item.prev:
    #         cache_item.prev.next = cache_item.next
    #         cache_item.next.prev = cache_item.prev

    # def move_node_to_tail(self, cache_item: CacheItem):
    #     self.take_node_out(cache_item)

    #     cache_item.prev = self.tail.prev
    #     cache_item.next = self.tail

    #     self.tail.prev.next = cache_item
    #     self.tail.prev = cache_item

    # def move_node_to_head(self, cache_item: CacheItem):
    #     self.take_node_out(cache_item)

    #     cache_item.prev = self.head
    #     cache_item.next = self.head.next

    #     self.head.next.prev = cache_item
    #     self.head.next = cache_item

    """
    solution 2 : using ordered dict
    """

    # def __init__(self, capacity: int):
    #     from collections import OrderedDict

    #     self.cache = OrderedDict()
    #     self.capacity = capacity

    # def get(self, key: int) -> int:
    #     if key not in self.cache:
    #         return -1

    #     # key as the newest one
    #     v = self.cache.pop(key)
    #     self.cache[key] = v
    #     return v

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.cache.pop(key)
    #         self.cache[key] = value
    #         return

    #     if len(self.cache) == self.capacity:
    #         self.cache.popitem(last=False)

    #     self.cache[key] = value

    """
    solution 3 : more concise solution
    """

    def __init__(self, capacity: int):
        self.cache: Dict[int, Node] = {}
        self.capacity = capacity
        self.size = 0
        self.head: Node = Node(0, 0)
        self.tail: Node = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_head(self, node: Node):
        self.take_node_out(node)
        self.insert_node_to_head(node)

    def take_node_out(self, node: Node):
        node.prev.next, node.next.prev = node.next, node.prev
        self.size -= 1
        self.cache.pop(node.key)

    def insert_node_to_head(self, node: Node):
        self.head.next.prev, self.head.next, node.prev, node.next = (
            node,
            node,
            self.head,
            self.head.next,
        )
        self.size += 1
        self.cache[node.key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.move_node_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.size == self.capacity:
                self.take_node_out(self.tail.prev)
            self.insert_node_to_head(Node(key, value))
        else:
            node = self.cache[key]
            node.val = value
            self.move_node_to_head(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
