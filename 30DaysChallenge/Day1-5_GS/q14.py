'''
Question: Minimum Size Subarray Sum
Input: A = [1, 4, 4], target = 4
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [4].
'''


class Solution:
    def minSubArrayLen(self, target: int, nums):
        left = 0
        mini = float('inf')
        right = 0
        curr_sum = 0
        while right < len(nums):
            curr_sum += nums[right]

            while curr_sum >= target:
                mini = min(mini, right-left+1)

                curr_sum -= nums[left]
                left += 1

            right += 1

        return 0 if mini == float('inf') else mini


if __name__ == '__main__':
    A = list(map(int, input().split()))
    target = int(input())
    ob = Solution()
    ans = ob.minSubArrayLen(target, A)
    print(ans)
