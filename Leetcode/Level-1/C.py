n = int(input())
person = 0
ans = []

while n > 0:
    event, num = list(input().split())
    num = int(num)

    if event == 'P':
        person += num
    if event == 'B':
        if num - person >= 1:
            print('YES')
            person = 0
        else:
            person -= num
            print('NO')
    n -= 1