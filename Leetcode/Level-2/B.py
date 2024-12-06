'''
    https://codeforces.com/problemset/problem/1721/A
'''
from collections import defaultdict
def B(map):
    if len(map) == 1: return 0
    if len(map) == 2: return 1
    if len(map) == 3: return 2
    if len(map) == 4: return 3

t = int(input())
while t > 0:
    map = defaultdict(int)
    for i in range(2):
        row = input()
        map[row[0]] += 1
        map[row[1]] += 1

    output = B(map)
    print(output)

    t -= 1