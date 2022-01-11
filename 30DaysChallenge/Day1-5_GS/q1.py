try:
    from collections import defaultdict

    class Solution:
        def Anagrams(self, words, n):
            dicti = defaultdict(list)
            for i in words:
                dicti[''.join(sorted(i))].append(i)
            ans = []
            for key, value in dicti.items():
                ans.append(dicti.get(key))
            return ans

    if __name__ == '__main__':
        t = int(input())
        for tcs in range(t):
            n = int(input())
            words = input().split()

            ob = Solution()
            ans = ob.Anagrams(words, n)

            for grp in sorted(ans):
                for word in grp:
                    print(word, end=' ')
                print()
except EOFError as e:
    print("")
