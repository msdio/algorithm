from sys import stdin

"""
완탐으로 하려면 어떻게 해야할까?
1높이에서 파괴하는 횟수,
2높이에서 파괴하는 횟수,
...
h높이에서 파괴하는 횟수

다 구해서 최소를 구하면 된다.
그러면 N*H 이니까 시간 안에 될 리가 없다.

장애물의 위치가 계속 변경되니까 imos를 떠올려야 한다.
첫번째 1이 석순이면 [1, 1]에 장애물이 생기고
두번째 5가 종유석이면 [h-5, h]에 장애물이 생기고
세번째 3가 석순이니 [1, 3]에 장애물이 생기고
...

이렇게 장애물 정보 업데이트는 O(N)에 된다.
그 뒤로 누적합은 O(N)에 되니까 충분히 가능할 것 같다.

시작점과 끝점의 정보를 구하면
psum[start] += 1
psum[end+1] -= 1
을 하면 된다.

그래서 석순인 경우에는
psum[0] += 1,
psum[i+1] -= 1 을 하면 되지만

종유석인 경우에는
psum[h-i] += 1을 하고,
맨 마지막에는 어차피 고려를 안해줘도 되니 굳이 -를 해줄 필요는 없다.
"""

n, h = map(int, stdin.readline().split())
obstacles = [0]
for _ in range(n):
    o = int(stdin.readline())
    obstacles.append(o)

# 종유석, 석순 정보 미리 업데이트 (imos)
psum = [0] * (h + 1)
for i in range(n + 1):
    if i % 2 == 0:  # 석순인 경우
        psum[1] += 1
        psum[obstacles[i] + 1] -= 1
    else:  # 종유석인 경우
        psum[h - obstacles[i] + 1] += 1

# 누적합 구하기
for i in range(1, h + 1):
    psum[i] = psum[i - 1] + psum[i]

# 최소값 구하기 (정답)
ans = 500001
cnt = 0
for i in range(1, h + 1):
    if psum[i] == ans:
        cnt += 1
        continue

    if psum[i] < ans:
        ans = psum[i]
        cnt = 1

print(ans, cnt)
