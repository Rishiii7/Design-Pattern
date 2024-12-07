'''
    https://codeforces.com/problemset/problem/2007/B
'''
def C(arr, operations, n, m):
    max_values = []
    max_val = max(arr)
    for c, l, r in operations:
        if c == '+': factor = 1
        else: factor = -1

        if l <= max_val <= r:
            max_val += factor
        max_values.append(max_val)

    return max_values
        
        
t = int(input())

while t > 0:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    operations = []
    for _ in range(m):
        c, l, r = input().split()
        l, r = int(l), int(r)
        operations.append((c, l, r))

    output = C(arr, operations, n, m)
    for val in output:
        print(val, end=' ')
 
    t-=1