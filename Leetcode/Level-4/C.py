
def C(x, n):
    if n == 0:
        return x 
    remainder = n % 4
    if x % 2 == 0:
        if remainder == 1:
            return x - n
        elif remainder == 2:
            return x + 1
        elif remainder == 3:
            return x + n + 1
        else: 
            return x
    else: 
        if remainder == 1:
            return x + n
        elif remainder == 2:
            return x - 1
        elif remainder == 3:
            return x - n - 1
        else: 
            return x

t = int(input())
while t > 0:
    x, n = map(int, input().split())
    output = C(x, n)
    print(output)

    t -= 1