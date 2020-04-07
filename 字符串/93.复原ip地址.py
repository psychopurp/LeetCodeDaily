#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start


class Solution:
    # def restoreIpAddresses(self, s: str) -> List[str]:
        # result = []

        # def check(track):
        #     if track == '':
        #         return False
        #     if (track[0] == '0' and len(track) > 1) or int(track) > 255:
        #         return False
        #     return True

        # def backtrack(nums, track, level=4):
        #     if level == 0:
        #         if len(nums) == 0:
        #             result.append(track[:-1])
        #         return

        #     for i in range(1, 3+1):
        #         if check(nums[:i]) and len(nums[:i]) == i:
        #             backtrack(nums[i:], track+nums[:i]+'.', level-1)

        # backtrack(s, '')
        # return result

    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)

        def valid(segment):
            if segment == '':
                return False
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def dfs(start=0, temp='', level=3):
            # if start == n and level == 0:
            #     result.append(temp[:-1])
            #     return
            if level == 0:
                if valid(s[start:]):
                    result.append(temp+s[start:])
                return

            for i in range(start, start+3):
                if i < n:
                    # dfs(i+1, temp+s[i]+'.', level-1)

                    if valid(s[start:i+1]):
                        dfs(i+1, temp=temp+s[start:i+1]+'.', level=level-1)

            return

        dfs(start=0, temp='')
        return result

# @lc code=end
