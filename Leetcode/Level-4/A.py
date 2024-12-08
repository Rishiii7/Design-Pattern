
def A(segments, n, m):
    count = 0
    points = []
    for i in range(1, m+1):
        flg = True
        for l , r in segments:
            if l <= i <= r: 
                flg = False
                break
        if flg:
            count += 1
            points.append(i)
            
    return (count, points)



n, m = map(int, input().split())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

output = A(segments, n, m)

print(output[0])
for num in output[1]:
    print(num, end=' ')
