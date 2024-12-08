def A(arr, n):
    k = 1
    pieces = 1
    total_pieces = 0
    happy = 0

    for i in range(n):
        total_pieces += arr[i]
        while total_pieces >= pieces:
            total_pieces -= pieces
            if total_pieces == 0:
                happy += 1
            k += 2
            pieces = 4 * k - 4
    
    return happy

        

t = int(input())
while t > 0 :
    n = int(input())
    arr = list(map(int, input().split()))

    output = A(arr, n)
    print(output)
    t -= 1