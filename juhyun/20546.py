import sys
input = sys.stdin.readline


money = int(input())
arr = list(map(int,input().split()))


def buy(mine_money, ju):
    buy_cnt = 0
    remain = mine_money
    if mine_money >= ju:
        buy_cnt = mine_money // ju
        remain = mine_money % ju
    return buy_cnt,remain


def sell(mine_money,mine_ju, ju):
    remain = ju * mine_ju + mine_money
    return remain

def last_day(mine_money, mine_ju, ju):
    res = ju * mine_ju + mine_money
    return res


# 준현
j_money = money
j_buy_count = 0
for i in range(len(arr)):
    # if arr[i] <=j_money:
        buy_cnt, j_money = buy(j_money,arr[i])
        j_buy_count += buy_cnt

# 성민
s_money = money
s_buy_count = 0

for i in range(3,len(arr)):
    if arr[i-3] < arr[i-2] and arr[i-2] < arr[i-1] and arr[i-1] < arr[i]:
        s_money = sell(s_money,s_buy_count, arr[i])
        s_buy_count = 0

    elif arr[i-3] > arr[i-2] and arr[i-2] > arr[i-1] and arr[i-1] > arr[i]:
        buy_cnt, s_money = buy(s_money, arr[i])
        s_buy_count += buy_cnt


res_j = last_day(j_money,j_buy_count, arr[-1])
res_s = last_day(s_money,s_buy_count, arr[-1])

if res_j == res_s:
    print('SAMESAME')
elif res_j > res_s :
    print('BNP')
elif res_j < res_s:
    print('TIMING')


