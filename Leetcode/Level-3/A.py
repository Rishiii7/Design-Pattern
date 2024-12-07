'''
    https://codeforces.com/problemset/problem/1843/A
'''
def A(arr, n):
    arr.sort()
    l, r = 0, n-1
    cost = 0

    while l < r:
        cost += arr[r] - arr[l]
        l += 1
        r -= 1
    return cost

t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    output = A(arr, n)
    print(output)

    t-=1