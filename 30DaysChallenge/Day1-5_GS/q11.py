'''
Question: Find Missing And Repeating
Input: 
arr: [1,3,4,5,6,7,8,9,10,10]
Output:
Missing: 2
Repeating: 10
Explanation:
The missing number is 2.
The repeating number is 10.

'''


class Solution:
    def findTwoElement(self, arr, n):
        sum = (n*(n+1))//2
        sum_sq = (n*(n+1)*(2*n+1))//6

        for i in range(n):
            sum -= arr[i]
            sum_sq -= arr[i]*arr[i]

        miss = (sum + sum_sq//sum)//2
        repeat = miss - sum
        return repeat, miss


if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc = tc-1
