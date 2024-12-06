'''
    https://codeforces.com/problemset/problem/892/A
'''

n = int(input())

rem_cola = list(map(int, input().split()))
cap_cans = list(map(int, input().split()))

largest, sec_larget = max(cap_cans[0], cap_cans[1]), min(cap_cans[0], cap_cans[1])
total_cola = sum(rem_cola)

for i in range(2, len(cap_cans)):
    if cap_cans[i] >= largest:
        sec_larget = largest
        largest = cap_cans[i]
    elif sec_larget <= cap_cans[i] < largest:
        sec_larget = cap_cans[i]

if total_cola > (largest + sec_larget): print('NO')
else: print('YES')
    