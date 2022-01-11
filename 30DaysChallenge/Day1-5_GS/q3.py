class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):

        if k <= 1:
            return 0

        left = 0
        right = 0
        prod = 1
        count = 0

        while right < n:
            prod *= a[right]
            while prod >= k:
                prod /= a[left]
                left += 1
            right += 1
            count += right - left

        return count


def main():
    T = int(input())
    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        print(Solution().countSubArrayProductLessThanK(arr, n, k))
        T -= 1


if __name__ == "__main__":
    main()
