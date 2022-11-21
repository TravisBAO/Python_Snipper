class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_str_length = len(x_str)
        x_reverse_str = ""
        for i in range(x_str_length):
            x_reverse_str += x_str[x_str_length -1 - i]
            
        return x_str == x_reverse_str
    


if __name__ == '__main__':
    myS = Solution()
    xyz = myS.isPalindrome(121)
    print(xyz)