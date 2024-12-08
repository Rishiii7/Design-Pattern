def B(str, n):
    divisors = []
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()

    def reverse_string(str1):
        return str1[::-1]

    new_str = str
    for num in divisors:
        new_str= reverse_string(new_str[:num]) + new_str[num:]

    return new_str

n = int(input())
str = input()

output = B(str, n)
print(output)