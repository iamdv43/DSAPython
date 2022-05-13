def maxProfit(n, price):
    fB = price[0]
    fS = 0
    sS = 0
    sB = 0
    for i in range(n):
        fB = min(fB, price[i])
        fS = max(fS, price[i] - fB)
        sB = max(sB, fS - price[i])
        if sB > 0:
            sS = max(sS, price[i] + sB)
    return sS if sS > 0 else fS


price = [1,2,1,2]
print(maxProfit(len(price), price))