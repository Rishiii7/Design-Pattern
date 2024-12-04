from collections import defaultdict
def D(n, brand_sum):

    prices = list(brand_sum.values())
    prices = sorted(prices, reverse=True)

    if len(prices) <= n:
        return sum(prices)
    else:
        return sum(prices[:n])

t = int(input())

while t > 0:
    n, k = map(int, input().split())
    brand_sum = defaultdict(int)
    for i in range(k):
        b, p = map(int, input().split())
        brand_sum[b] += p
    
    output = D(n, brand_sum)
    print(output)
    t -= 1
