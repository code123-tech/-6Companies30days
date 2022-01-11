'''
n: 10
to return : 12
'''


class Solution:
    def getNthUglyNo(self, n):

        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while len(ugly) < n:
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            ugly.append(min(u2, u3, u5))
            if u2 == ugly[-1]:
                i2 += 1
            if u3 == ugly[-1]:
                i3 += 1
            if u5 == ugly[-1]:
                i5 += 1
        return ugly[-1]


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n)
        print(ans)
        tc -= 1
