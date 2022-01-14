'''
Question: Given a pattern containing only I's and D's. I for increasing and D for decreasing.
Devise an algorithm to print the minimum number following that pattern.

Input: D 
Output: 21 

Input: IIDDD
IIDDD
Output:
126543
Explanation:
Above example is self- explanatory,
1 < 2 < 6 > 5 > 4 > 3
  I - I - D - D - D
'''


class Solution:
    def printMinNumberForPattern(self, S):
        pass


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        S = str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
