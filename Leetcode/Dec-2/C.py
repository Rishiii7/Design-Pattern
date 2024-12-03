def C(row1, row2, n):
    total = 0

    max_among_smallest = float('-inf')

    for i in range(n):
        if row1[i] > row2[i]:
            total += row1[i]
            max_among_smallest = max(max_among_smallest, row2[i])
        else:
            total += row2[i]
            max_among_smallest = max(max_among_smallest, row1[i])
    
    return total + max_among_smallest


# Input handling
t = int(input())
while t > 0:
    n = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))

    output = C(row1, row2, n)
    print('output:', output)
    t -= 1
