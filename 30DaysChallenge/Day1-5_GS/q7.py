'''
Question: Find the position of M-th item 
Input: N = 5, M = 8, K = 2 
Output: 2
'''


class Solution:
    def findPosition(self, N, M, K):
        remainingPositions = N - K + 1

        if M <= remainingPositions:
            return K + M - 1

        M = M - remainingPositions

        if M % N == 0:
            return N

        return M % N


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M, K = map(int, input().split())

        ob = Solution()
        print(ob.findPosition(N, M, K))
