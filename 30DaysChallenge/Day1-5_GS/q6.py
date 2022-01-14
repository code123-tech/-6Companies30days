'''
Question: Greatest Common Divisor of Two Strings 
Input: str1 = "ABCABC", str2 = "ABC"
Output: ABC
'''
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2 + str1:
            return ""

        gcd = math.gcd(len(str1), len(str2))

        return str1[:gcd]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    ob = Solution()
    print(ob.gcdOfStrings(str1, str2))
