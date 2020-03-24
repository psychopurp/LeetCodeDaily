#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''第一种解法 runtime:86.53% memory:12.35% '''
        for i in reversed(range(len(digits))):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                if i==0:
                    digits.insert(0,1)
                    return digits
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     '''第二种解法 runtime:42.63% memory:12.35% '''
    #     nums=int(''.join(str(i) for i in digits))+1
    #     return [int(i) for i in str(nums)]           
# @lc code=end



