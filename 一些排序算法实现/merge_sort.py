
import random


def generate_rand(num):
    result = []
    for i in range(num):
        result.append(random.randint(0, 100))
    return result


def merge_sort(nums, low, high):
    '''
    时间复杂度O(n logn)
    空间复杂度O(n)
    '''

    def merge(nums, low, high):
        tmp = nums[low:high + 1]
        i = low
        high = len(tmp)-1
        left = 0
        mid = (0+high) // 2
        # 额外开辟空间，拷贝num[l,..,r]到tmp数组，然后在原nums上赋值操作
        right = mid+1
        i = low
        while left <= mid and right <= high:
            if tmp[left] < tmp[right]:
                nums[i] = tmp[left]
                left += 1
            else:
                nums[i] = tmp[right]
                right += 1
            i += 1
        while left <= mid:
            nums[i] = tmp[left]
            left += 1
            i += 1
        while right <= high:
            nums[i] = tmp[right]
            right += 1
            i += 1

    if low < high:
        mid = (low+high)//2
        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, high)


def main():
    data = generate_rand(100)
    # data = [1]
    sorted_data = merge_sort(data, 0, len(data) - 1)
    print(data)


if __name__ == "__main__":
    main()
