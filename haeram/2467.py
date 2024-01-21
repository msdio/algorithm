from sys import stdin

'''
모두 조합할거면 100000C2..? 절대 안된다.

정렬하고 투 포인터를 하려고 고민해봤는데 마땅히 해결책이 될 것 같진 않다.

합이 0이 될라면 크기(절댓값) 순으로 정렬하면 되나?
정렬 하고 내 양옆이랑만 비교하면 되는건가
딱히 반례가 없는 것 같다.
'''

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

arr.sort(key=lambda x: abs(x))

cur_max = 2 * 10**9
ans = []
for i in range(1, n):
    cand = abs(arr[i-1] + arr[i])

    if cand < cur_max:
        ans = [[arr[i-1], arr[i]]]
        cur_max = cand
        continue

    if cand == cur_max:
        ans.append([arr[i-1], arr[i]])
        continue

temp = ans[0]
temp.sort()

print(*temp)
