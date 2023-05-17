from sys import stdin

x, y = map(int, stdin.readline().split())
z = int(y * 100 / x)

start = 0
end = 1000000000

while start <= end:
    mid = int((start+end) / 2)
    cur_z = int((y+mid) * 100 / (x+mid))

    if cur_z > z:
        end = mid-1
    else:
        start = mid+1

if start > 1000000000:
    print(-1)
else:
    print(start)
