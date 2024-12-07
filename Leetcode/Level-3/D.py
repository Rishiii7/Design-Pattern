'''
    https://codeforces.com/contest/1238/problem/A
'''
def D(x,y):
    diff = x - y
    if diff < 2: return 'NO'
    else: return 'YES'

t = int(input())

while t > 0:
    x, y = map(int, input().split())
    output = D(x, y)
    print(output)
 
    t-=1