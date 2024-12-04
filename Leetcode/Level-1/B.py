def precompute_sequences(max_n):
    sequences = {}
    for n in range(1, max_n + 1):
        a = []
        for i in range(1, n + 1):
            candidate = max(a[-1] + 1 if a else 1, i)
            while any(candidate % i == a[j] % (j + 1) for j in range(len(a))):
                candidate += 1
            a.append(candidate)
        sequences[n] = a
    return sequences

# Precompute sequences for n from 1 to 51
pre_seq = precompute_sequences(51)

def B(n):
    return pre_seq[n]

t = int(input())
while t > 0:
    n = int(input())
    output = B(n)
    
    # print output
    for num in output:
        print(num, end=' ')

    t -= 1