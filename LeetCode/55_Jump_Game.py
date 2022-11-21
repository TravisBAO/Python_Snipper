# -*- coding: utf-8 -*- 
# @Time : 4/5/2022 1:09 AM
# @Author : BaoYi-Travis
# @Version:
# @Function:

class Solution:
    def canJump(self, nums):
        lengthnums = len(nums)
        k = 0
        for i in range(lengthnums-1):
            if i > k:
                return False
            if k >= lengthnums - 1:
                return True
            k = max(k, nums[i] + i)


if __name__ == '__main__':
    listUnderTest = [2,2,3]
    myS = Solution()

    print(myS.canJump(listUnderTest))
