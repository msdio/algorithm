from sys import stdin

n = int(stdin.readline())
times = []

for _ in range(n):
    time = list(map(int, stdin.readline().split()))
    times.append(time)


def calculate_time(arr, start, end):
    total_times = [0 for _ in range(end - start + 1)]

    for time in arr:
        for i in range(time[0], time[1]):
            total_times[i - start] = 1

    return total_times.count(1)


ans = 0
start, end = 1000, 0
for t in times:
    start = min(start, t[0])
    end = max(end, t[1])

for i in range(n):
    cand = list(filter(lambda x: x != times[i], times))

    cnt = calculate_time(cand, start, end)

    ans = max(ans, cnt)

print(ans)
