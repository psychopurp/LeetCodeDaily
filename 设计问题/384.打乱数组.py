#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random
        array = list(self.nums)

        for i in range(len(array)):
            index = random.randint(i, len(array) - 1)
            array[i], array[index] = array[index], array[i]
        return array

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
