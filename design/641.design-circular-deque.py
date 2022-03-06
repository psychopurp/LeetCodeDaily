#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.front, self.rear = 0, 0
        self.buffer = [-1]*k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.buffer[self.front] = value
        else:
            self.front = (self.front-1) % self.capacity
            self.buffer[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        if self.isEmpty():
            self.buffer[self.rear] = value
        else:
            self.rear = (self.rear+1) % self.capacity
            self.buffer[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.buffer[self.front] = -1
        self.front = (self.front+1) % self.capacity
        self.size -= 1

        if self.isEmpty():
            self.rear = self.front
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.buffer[self.rear] = -1
        self.rear = (self.rear-1) % self.capacity
        self.size -= 1

        if self.isEmpty():
            self.front = self.rear
        return True

    def getFront(self) -> int:
        return self.buffer[self.front]

    def getRear(self) -> int:
        return self.buffer[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end
