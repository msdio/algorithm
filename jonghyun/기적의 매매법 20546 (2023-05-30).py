asset = int(input())
prices = list(map(int, input().split()))

bnp = asset
timing = asset


plus = 0
minus = 0
stock = 0
stock2 = 0
before = -1
for price in prices :
    if before != -1 and before > price:
        minus += 1
        plus = 0
    
    if before != -1 and before < price:
        plus += 1
        minus = 0
    
    if before != -1 and before == price :
        plus = 0
        minus = 0
    
    if minus >= 3 :
        stock_plus = asset // price
        if stock_plus > 0 :
            asset -= stock_plus * price
            stock += stock_plus

    if plus >= 3 :
        while stock > 0 :
            stock -= 1
            asset += price
    
    before = price

for price in prices :
    if price <= bnp :
        stock2 += (bnp // price)
        bnp -= (bnp // price) * price

if stock2 * prices[-1] + bnp > stock * prices[-1] + asset :
    print("BNP")
elif stock2 * prices[-1] + bnp < stock * prices[-1] + asset :
    print("TIMING")
else :
    print("SAMESAME")