from sys import stdin

n = stdin.readline()
houses = list(map(int, stdin.readline().split()))
houses.sort()

house_len = len(houses)

mid = 0
if (house_len % 2 == 1):
    mid = (house_len - 1) / 2
else:
    mid = house_len / 2 - 1

print(houses[int(mid)])
