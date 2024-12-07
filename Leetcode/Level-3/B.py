'''
    https://codeforces.com/problemset/problem/1466/B
'''
def B(arr, n):
    map = [0] * (max(arr) + 2)
    for num in reversed(arr):
        if map[num+1] == 0:
            map[num+1] += 1
        else:
            map[num] += 1
    
    diff = 0
    for num in map:
        if num > 0:
            diff += 1
    return diff


t = int(input())

while t > 0:
    n = int(input())
    arr = list(map(int, input().split()))

    output = B(arr, n)
    print(output)

    t-=1