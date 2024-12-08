def twice(arr, n):
    score = 0
    arr.sort()
    i = 0
    while i < n-1:
        if arr[i] == arr[i+1]:
            score += 1
            i += 2
        else:
            i += 1
    return score


t = int(input())
while t > 0 :
    n = int(input())
    arr = list(map(int, input().split()))
    
    output = twice(arr, n)
    print(output)
    t -= 1