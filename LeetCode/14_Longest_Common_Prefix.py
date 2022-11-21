# -*- coding: utf-8 -*- 
# @Time : 4/5/2022 10:26 AM
# @Author : BaoYi-Travis
# @Version:
# @Function:

class Solution:
    def longestCommonPrefix(self, strs):
        lengthList = []
        commonPrefix = ""

        # get the length of the shortest string in list
        for i in range(len(strs)):
            lengthList.append(len(strs[i]))
        shortestStringLen = min(lengthList)
        # get the shortest string in list
        shortestString = strs[lengthList.index(shortestStringLen)]
        
        m = ""
        for i in range(shortestStringLen):
            c = 0
            for j in range(len(strs)):
                if shortestString[i] == strs[j][i]:
                    c += 1
                    m = shortestString[i]
            if c == len(strs):
                commonPrefix += m
            else:
                break
        return commonPrefix


if __name__ == '__main__':
    myS = Solution()
    stringList = ["fly", "flye", "fly4"]
    print(myS.longestCommonPrefix(stringList))


