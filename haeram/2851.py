from sys import stdin

mushroom = []
for _ in range(10):
    score = int(stdin.readline())
    mushroom.append(score)

ans = 0
for m in mushroom:
    if (ans + m >= 100):
        if (abs(100-ans) < abs(ans+m-100)):
            ans = ans
        else:
            ans = ans + m

        break

    ans += m

print(ans)
