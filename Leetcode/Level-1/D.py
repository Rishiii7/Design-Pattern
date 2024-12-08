from collections import defaultdict
# def D(n, brand_sum):

#     prices = list(brand_sum.values())
#     prices = sorted(prices, reverse=True)

#     if len(prices) <= n:
#         return sum(prices)
#     else:
#         return sum(prices[:n])

def D(n, k, brand_sum):
    brand_sum = sorted(brand_sum, reverse=True)
    return sum(brand_sum[:min(n, k)])


t = int(input())

while t > 0:
    n, k = map(int, input().split())
    brand_sum = [0] * (k + 1)
    for i in range(k):
        b, p = map(int, input().split())
        brand_sum[b] += p
    
    output = D(n, k, brand_sum)
    print(output)
    t -= 1
