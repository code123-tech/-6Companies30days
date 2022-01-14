'''
Question: Array Pair Sum Divisibility Check
Input: A = [1, 4, 3, 2], K = 4
Output: True
'''

from collections import defaultdict


class Solution:
    def canPair(self, arr, k):
        n = len(arr)
        if n & 1:
            return False

        count = defaultdict(int)
        for i in range(n):
            count[arr[i] % k] += 1

        for number in count:
            if number == 0 and count[number] & 1:
                return False

            if number != 0 and count[k-number] != count[number]:
                return False

        return True


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.canPair(nums, k)
        if(ans):
            print("True")
        else:
            print("False")
