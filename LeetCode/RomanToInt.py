class Solution:
    def romanToInt(self, s: str) -> int:
        map_dict = {
            "I":    1,
            "V":    5,
            "X":    10,
            "L":    50,
            "C":    100,
            "D":    500,
            "M":    1000,
            "IV":   4,
            "IX":   9,
            "XL":   40,
            "XC":   90,
            "CD":   400,
            "CM":   900,
        }
        
        n = 0
        c = len(s) + 1
        for i in range (0, len(s)):
            if c == i:
                continue
            if s[i:i+2] in map_dict:
                n += map_dict[s[i:i+2]]
                c = i +1
            else:
                n += map_dict[s[i]]
                
        return n
        
if __name__ == '__main__':
    myRI = Solution()
    inputX = "MCMXCIV"
    x = myRI.romanToInt(inputX)
    print(x)