
import random


def generate_rand(num):
    result = []
    for i in range(num):
        result.append(random.randint(0, 100))
    return result


def partition_left(nums, low, high):
    # 取左边第一位
    '''high为最后一个元素下标，函数返回基准值'''
    pivot = nums[low]
    while low < high:
        # 从右边找比它小的
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
        # 从左边找比它大的
        while low < high and nums[low] <= pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    return low


def partition_right(nums, low, high):
    # 取左边第一位
    '''high为最后一个元素下标，函数返回基准值'''
    pivot = nums[high]
    while low < high:
        while low < high and nums[low] <= pivot:
            low += 1
        nums[high] = nums[low]
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
    nums[low] = pivot
    return low


def quick_sort(nums, low, high):
    '''时间复杂度 O(nlog n)'''
    if low < high:
        base = partition_right(nums, low, high)
        quick_sort(nums, low, base - 1)
        quick_sort(nums, base+1, high)


def quick_sort_2(nums):
    '''空间复杂度O(N)'''
    if len(nums) <= 1:
        return nums

    pivot = nums.pop()
    lesser, greater = [], []
    for i in nums:
        if i > pivot:
            greater.append(i)
        else:
            lesser.append(i)
    return quick_sort_2(lesser)+[pivot]+quick_sort_2(greater)


if __name__ == "__main__":
    data = generate_rand(1000)
    quick_sort(data, 0, len(data) - 1)
    # result = quick_sort_2(data)
    print(data)
