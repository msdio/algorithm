n, m = list(map(int, input().split()))

min_six = 0xFFFFFF
min_one = 0xFFFFFF
for i in range(m) :
    six, one = list(map(int, input().split()))
    min_one = min(one, min_one)
    min_six = min(six, min_six)

if min_six >= min_one * 6 :
    min_six = min_one * 6

tmp = 0
while n >= 6 :
    tmp += min_six
    n -= 6

answer = tmp

for i in range(n) :
    answer += min_one

print(min(answer, tmp + min_six))