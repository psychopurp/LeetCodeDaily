

class BinaryHeap:
    '''一个二叉堆，小顶堆 利用列表实现'''

    def __init__(self, max_size=100):
        # 初始值设置一个无限小的哨兵
        self.__heap = [float('-inf')]
        self.max_size = max_size

    def __len__(self):
        '''求长度'''
        return len(self.__heap)-1

    def insert(self, *data):
        '''向堆中插入元素'''
        if len(self)+len(data) > self.max_size:
            raise ValueError("堆已满，插入失败")
        for x in data:
            self.__heap.append(x)
            self.__siftup(len(self))
        print("插入成功")

    def __siftup(self, idx):
        '''最后插入的元素上浮'''
        pos = idx
        x = self.__heap[idx]
        # 此处可以体现出哨兵的作用了, 当下标为0时, x一定大于inf
        while x < self.__heap[pos // 2]:
            self.__heap[pos] = self.__heap[pos // 2]
            pos = pos//2
        self.__heap[pos] = x

    def __siftdown(self, idx):
        '''序号为i的元素下沉'''
        x = self.__heap[idx]
        length = len(self)
        while True:
            child_idx = idx * 2
            if child_idx > length:
                break
            # 有两个子节点的情况 而且右边节点较小,不然和左节点交换
            if child_idx != length and self.__heap[child_idx] > self.__heap[child_idx + 1]:
                child_idx += 1
            # 如果父节点大于子节点 ，则交换
            if x > self.__heap[child_idx]:
                self.__heap[idx] = self.__heap[child_idx]
                idx = child_idx
            else:
                break
        self.__heap[idx] = x

    def get_min(self):
        if len(self) == 0:
            raise ValueError("堆为空")
        return self.__heap[1]

    def delete_min(self):
        '''删除堆顶元素 时间复杂度O(log n)'''
        _min = self.get_min()
        last = self.__heap.pop()
        # 为空就不需要下浮
        if len(self) != 0:
            self.__heap[1] = last
            self.__siftdown(1)
        return _min

    def create_heap(self, data):
        '''直接创建一个小顶堆，接收一个iterable对象参数，效果同insert，效率比insert一个个插入高，时间复杂度为O(n)'''
        self.__heap.extend(data)
        # 从倒数第二层开始 下沉
        for idx in range(len(self) // 2, 0, -1):
            self.__siftdown(idx)

    def clear(self):
        '''清空堆'''
        self.__heap = [float('-inf')]

    def update_key(self, idx, key):
        '''更新指定位置的元素,idx>=1'''
        if idx > len(self) or idx < 1:
            print("索引超出堆的数量或小于1")
            return
        x = self.__heap[idx]
        self.__heap[idx] = key
        if key > x:
            self.__siftdown(idx)
        else:
            self.__siftup(idx)

    def delete_key(self, idx):
        '''删除指定位置的元素,idx>=1'''
        if idx > len(self) or idx < 1:
            print('索引超出堆的数量或小于1')
            return
        last = self.__heap.pop()
        if len(self):
            self.__heap[idx] = last
            self.__siftdown(idx)

    def show(self):
        print(self.__heap[1:])


def heap_sort(data, reverse=False):
    '''堆排序'''
    heap = BinaryHeap(max_size=len(data))
    heap.create_heap(data)
    result = []
    for i in range(len(heap)):
        # 时间复杂度O(log n)
        result.append(heap.delete_min())
    if reverse:
        return result[::-1]
    return result


def get_k_big_nums(data, k):
    '''获取前k个最大的数 时间复杂度O(nlog k)'''
    heap = BinaryHeap(k)
    heap.create_heap(data[:k])
    for i in data[k:]:
        if i > heap.get_min():
            heap.update_key(1, i)
    result = []
    for i in range(k):
        result.append(heap.delete_min())
    return result


def main():
    # heap = BinaryHeap()
    # heap.insert(0, 1, 2)
    # heap.show()
    # heap.update_key(1, -3)
    # heap.show()
    data = [1, 2, 5, 2, 4, 10, 7, 1, 3, 5, 9]
    result = get_k_big_nums(data, 3)
    print(result)


if __name__ == "__main__":
    main()
