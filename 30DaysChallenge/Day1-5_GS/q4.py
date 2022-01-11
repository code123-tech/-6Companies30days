'''
arr: wwwwaaadexxxxxx
to return: w4a3d6e1x6
'''


def encode(arr):
    if len(arr) == 0:
        return ''

    res = ''
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            count += 1
        else:
            res += arr[i-1] + str(count)
            count = 1
    res += arr[-1] + str(count)
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip()
        print(encode(arr))
