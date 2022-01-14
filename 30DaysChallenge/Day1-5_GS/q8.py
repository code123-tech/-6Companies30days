'''
Question: Total Decoding Ways
Input: 123
Output: 3
Explanation: "123" can be decoded as "ABC"(123), "LC"(12 3) and "AW"(1 23).
'''


import sys


class Solution:
    def CountWays(self, str):
        one, two, three = 0, 0, 0
        if str[0] != "0":
            three += 1
        for i in range(1, len(str)):
            one, two, three = two, three, 0
            first, second = int(str[i]), int(str[i-1:i+1])
            if 1 <= first <= 9:
                three += two
            if 10 <= second <= 26:
                if i-2 >= 0:
                    three += one
                else:
                    three = three + 1

        return three % (10**9+7)


sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.CountWays(str)
        print(ans)
