N, M = list(map(int, input().split()))

meats = []
for i in range(N) :
    m, n = tuple(map(int, input().split()))
    meats.append((n, m))

meats.sort(key = lambda x : (x[0], -x[1]))
# print(meats)
meat_weight_sum = 0
present_meat_price = -1
answer = INF = 0xFFFFFFFFFFFFFF
present_price = 0
for price, weight in meats :
    if present_meat_price < price :
        
        present_meat_price = price
        present_price = price
        meat_weight_sum += weight
    else : # 무게가 전하고 같은 경우
        present_price += price
        meat_weight_sum += weight
    # print(f"weight,price, {weight}, {price}, {meat_weight_sum}, {}")
    if meat_weight_sum >= M :
        answer = min(present_price, answer)

if answer != INF :
    print(answer)
else :
    print(-1)



'''
7 9
1 2
4 3
2 4
4 8
3 6
3 9
3 19
# 8

10 10
1 33
1 21
1 2
1 4
1 9
1 20
1 33
1 1
1 4
1 5
# 132

11 10
1 10
1 9
1 8
1 7
1 6
1 5
1 4
1 3
1 2
1 1000
2 1000000
# 1054

3 1000
3 10
3 9
3 8
# -1

3 100
50 10
50 9
50 8
# 17

3 101
50 10
50 9
50 8
# 27

4 9
1 2
2 4
3 6
4 8
# 8

6 13
1 2
2 4
3 6
4 8
5 10
6 12
# 10 

1 10
10 1
# 1

10 1
1 1
1 2
1 3
1 4
1 5
1 6
1 7 
1 8
1 9
1 10
# 1

10 2
1 1
1 2
1 3
1 4
1 5
1 6
1 7 
1 8
1 9
1 10
# 3

10 2
1 1
1 2
1 3
1 4
1 5
1 6
1 7 
1 8
1 9
1 10
# 3

10 5011
1 1
1 2
2 128934172489
3 4
5102 395903092
1 6
1 7 
1 8
1 9
1 10
# 395903092

12 11
1 1
1 2
2 128934172489
3 4
5102 395903092
1 6
1 7 
1 8
1 9
1 10
100 111111111
1 11


5 13
1 2
6 6
2 4
3 6
4 8

5 12
1 2
6 6
2 4
3 6
4 8

'''