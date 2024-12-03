from collections import Counter
def B(s, n):
    freq = Counter(s)

    char_list = [k for k, _ in sorted(freq.items(), key=lambda x : x[1], reverse=True)]
    max_char = char_list[0]
    min_char = char_list[-1]

    res_list = list(s)
    for idx, ch in enumerate(res_list):
        if ch == min_char:
             res_list[idx] = max_char
             break
    return ''.join

    
t = int(input())
while t > 0 :
    n = int(input())
    s = input()

    output = B(s, n)
    print('output: ', output)
 