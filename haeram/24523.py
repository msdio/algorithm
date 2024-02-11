from sys import stdin

'''
완탐은 10^12라서 절대 안된다.

prev, next가 같을 동안 계속 i 값 증가시키다가
달라지면 (현재 인덱스) 를 next-prev 개 만큼 넣는다.
그리고 prev, next를 next+1로 업데이트 한다.

만약에 prev가 n이상이 되면 n-prev 만큼 -1을 넣는다.
'''

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

if n == 1:
    print(-1)
else:
    ans = []

    prev, next = 0, 1
    while prev < n and next < n:
        if arr[prev] == arr[next]:
            next += 1
            continue
        else:
            ans += [next+1] * (next-prev)
            prev = next
            next += 1
            continue

    ans += [-1] * (n-prev)

    print(*ans)
