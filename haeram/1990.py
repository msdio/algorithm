from sys import stdin

"""
10^8 이니까 10^4까지 소수를 구한다.

## 팰린드롬
1. 한자리수이면 팰린드롬
2. 두자리수는 팰린드롬검사 필요없음
3. 세자리수부터 팰린드롬 검사 필요

## 소수
약수 개수를 세서 약수가 없는지 확인한다 (2 ~ n-1까지)
"""

a, b = map(int, stdin.readline().split())


def is_pal(num):  # 팰린드롬 구하기
    convert = str(num)
    len_convert = len(convert)

    if len_convert == 1:
        return True

    front = convert[: len_convert // 2]
    rear = ""
    if len_convert % 2 == 0:
        rear = convert[-len_convert // 2 :]
    else:
        rear = convert[-len_convert // 2 + 1 :]

    if front == rear[::-1]:
        return True
    else:
        return False


def is_prime(n):
    flag = True
    for i in range(2, n + 1):
        if i * i > n:
            break

        if n % i == 0:
            flag = False
            break

    return flag


# main
cands = []
ans = []
max_num = min(b, 10_000_000)
for i in range(a, max_num + 1):
    if is_pal(i):
        cands.append(i)

for cand in cands:
    if is_prime(cand):
        print(cand)

print(-1)
