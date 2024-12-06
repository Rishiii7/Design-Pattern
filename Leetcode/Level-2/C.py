'''
    https://codeforces.com/problemset/problem/1537/A
'''
max_int = 10 ** 4
def C(arr, n):
    total_sum  = sum(arr)
    if total_sum >= n: return total_sum - n
    else:
        return 1
    

t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    output = C(arr, n)
    print(output)

    t -= 1