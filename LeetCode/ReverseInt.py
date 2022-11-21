class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x)
        if x>0:
            x_str_reverse = str(x)[::-1]
            x_reverse = int(x_str_reverse)
        else:
            x_str_reverse = str(abs(x))[::-1]
            x_reverse = int(x_str_reverse)
            x_reverse = x_reverse - 2 * x_reverse
        if x_reverse not in [-2**31, 2**31-1]:
            return 0
        else:
            return x_reverse

if __name__ == '__main__':
    myS = Solution()
    print(myS.reverse(123))
    print(myS.reverse(-234))
