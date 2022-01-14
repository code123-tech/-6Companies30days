'''
Suppose you are given a list of more than 10 numbers. 
You have to find 10 maximum numbers from that list. 
'''

import heapq


class Solution:
    def get10MaximumNumbers(self, lst):
        temp = []
        length = len(lst)
        if length < 10:
            return lst
        for i in range(10):
            heapq.heappush(temp, lst[i])

        for i in range(10, length):
            root = heapq.heappop(temp)
            if lst[i] > root:
                heapq.heappush(temp, lst[i])
            else:
                heapq.heappush(temp, root)
        return temp


if __name__ == '__main__':
    # tc = int(input())
    tc = 1
    while tc > 0:
        lst = list(map(int, input().split()))
        ob = Solution()
        ans = ob.get10MaximumNumbers(lst)
        print(ans)
        tc -= 1
