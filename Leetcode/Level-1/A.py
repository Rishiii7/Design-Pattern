def A(s):
    fir = s[0]
    operator = s[1]
    sec = s[2]

    if sec > fir: return fir + '<' + sec
    elif sec < fir: return fir + '>' + sec
    elif sec == fir : return fir + '=' + sec


t = int(input())

while t > 0:
    s = input()

    output = A(s)
    print(output)

    t -= 1
