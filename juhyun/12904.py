# 구현, 문자열, 그리디
# 시간복잡도 먼저 계산하고 풀기💦
# 역발상 🔥
import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]
print(1 if T == S else 0)