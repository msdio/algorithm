from sys import stdin

'''
일단 x, y값을 다 dictionary에 저장해두고

(x, y)가 나왔을 때
(x+a, b), (x, b+y), (x+a, y+b)가 모두 있는지 확인하면 된다.

근데 좌표를 저장해야 하니까 딕셔너리는 안될 것 같고.. 배열에 저장해야 겠다
'''

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())

points = set()
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    points.add((x, y))

ans = 0
for point in points:
    x, y = point

    if (x+a, y) not in points:
        continue

    if (x, b+y) not in points:
        continue

    if (x+a, b+y) not in points:
        continue

    ans += 1


print(ans)
