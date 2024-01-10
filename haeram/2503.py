from sys import stdin
from itertools import permutations

n = int(stdin.readline())
tries = [list(map(int, stdin.readline().split())) for _ in range(n)]

indexes = [str(i) for i in range(1, 10)]
cands = list(permutations(indexes, 3))

ans = 0
for cand in cands:
    flag = True

    for nums, strike, ball in tries:
        nums = list(str(nums))

        strike_cnt = 0
        ball_cnt = 0

        for i in range(3):
            if cand[i] == nums[i]:
                strike_cnt += 1
            else:
                if nums[i] in cand:
                    ball_cnt += 1

        if (strike_cnt != strike or ball_cnt != ball):
            flag = False
            break

    if (flag):
        ans += 1

print(ans)
