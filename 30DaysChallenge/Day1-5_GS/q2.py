# User function Template for python3

class Solution:
    def doOverlap(self, L1, R1, L2, R2):
        r1X1, r1Y1 = L1
        r2X1, r2Y1 = L2
        r1X2, r1Y2 = R1
        r2X2, r2Y2 = R2

        bottomX = max(r1X1, r2X1)
        bottomY = max(r1Y2, r2Y2)
        topX = min(r1X2, r2X2)
        topY = min(r1Y1, r2Y1)

        if (bottomX <= topX and bottomY <= topY):
            return 1
        return 0


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p = [0]*2
        q = [0]*2
        r = [0]*2
        s = [0]*2
        p[0], p[1], q[0], q[1], r[0], r[1], s[0], s[1] = map(
            int, input().strip().split(" "))
        ob = Solution()
        ans = ob.doOverlap(p, q, r, s)
        print(ans)
