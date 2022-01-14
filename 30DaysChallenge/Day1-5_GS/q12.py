'''
Question: Find the total number of sqaures in the given chessboard
Input: 
N: 2
Output: 5
'''


class Solution:
    def squaresInChessBoard(self, N):
        return ((N*(N+1))//2*(2*N+1)//3)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.squaresInChessBoard(N))
