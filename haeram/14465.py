from sys import stdin
import sys

'''
살아있는 신호등은 1, 망가진건 0으로 배열을 하나 만든다음에
K만큼의 길이로 검사하면서 그 안에 0이 몇개 있는지 센다
0을 만나면 바로 return

근데 원형이니까.. 배열 길이를 2배로 만들어서 하면 되겠다
'''

n, k, b = map(int, stdin.readline().split())

arr = [1 for _ in range(n+1)]
arr += (arr[1:])
for _ in range(b):
    broken = int(stdin.readline())
    arr[broken] = 0
    arr[broken+n] = 0

if k == n:
    print(b)
    sys.exit(0)

ans = 10**6 + 1
for i in range(1, 2*(n+1)-k):
    cur_cnt = arr[i: i+k].count(0)

    if (cur_cnt == 0):
        ans = 0
        break

    ans = min(ans, cur_cnt)

print(ans)
