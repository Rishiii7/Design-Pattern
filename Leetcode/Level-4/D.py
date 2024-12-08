def D(mat, n):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def can_place(i, j):
        for dr, dc in directions:
            r, c = i + dr, j + dc
            if not (0 <= r < n and 0 <= c < n) or mat[r][c] == '#':
                return False
        return True
    
    def place(i, j):
        mat[i][j] = '#'
        for dr, dc in directions:
            r, c = i + dr, j + dc
            mat[r][c] = '#'

    for i in range(n):
        for j in range(n):
            if mat[i][j] == '#': continue

            if can_place(i, j):
                place(i, j)
    
    for i in range(n):
        for j in range(n):
            if mat[i][j] == '.':
                return 'NO'

    return 'YES' 


n = int(input())
mat = []
for _ in range(n):
    row = list(input().strip()) 
    mat.append(row)

output = D(mat, n)
print(output)