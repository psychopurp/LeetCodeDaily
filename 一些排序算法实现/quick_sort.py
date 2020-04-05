
import random


def generate_rand(num):
    result = []
    for i in range(num):
        result.append(random.randint(0, 100))
    return result


def quick_sort(nums, low, high):
    # 返回基准值
    def partition(nums, low, high):
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

    if low < high:
        base = partition(nums, low, high)
        quick_sort(nums, low, base - 1)
        quick_sort(nums, base+1, high)


if __name__ == "__main__":
    data = generate_rand(1000)
    quick_sort(data, 0, len(data) - 1)
    print(data)
