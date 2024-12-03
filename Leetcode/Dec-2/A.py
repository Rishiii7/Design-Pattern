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
    
    return ha