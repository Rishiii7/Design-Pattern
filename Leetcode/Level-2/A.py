'''
    https://codeforces.com/problemset/problem/1492/A
'''

def A(n, a, b, c):
    i = a if n < a else a * (n // a)
    j = b if n < b else b * (n // b)
    k = c if n < c else c * (n // c)
    if i == 0 or j == 0 or k == 0:  return 0
    min_time = float('inf')

    while i < n:
        i += a
    min_time = min(min_time, i-n)

    while j < n:
        j += b
    min_time = min(min_time, j-n)
    
    while k < n:
        k += c
    min_time = min(min_time, k-n)

    return min_time


t = int(input())

while t > 0:
    n, a, b, c = map(int, input().split())
    output = A(n, a, b, c)

    print(output)

    t -= 1