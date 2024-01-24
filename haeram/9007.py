from sys import stdin

"""
완전 탐색으로 한다면
(한 반에서 모든 사람을 뽑는 경우의 수)^4 이니까
1000^4 * T 이니까, 10^12 * T이다.

그럼 세제곱은 되나? 세제곱이 된다면 
나머지 세 반의 모든 합쳐지는 경우의 수를 구하고
남은 한 반하고 합쳐보면서 최대값을 찾으면 된다. 이걸 4번 반복하면 됨

근데 세제곱이어도 안되네

아 그럼 두개씩 합치는건 되나
1000^2 * 2 = 10^6 * 2 * T 이긴 한데 T가 150보다 크지 않기를 바라는 수 밖에 없을듯..?

근데 두 개씩 합치고 나면 합친 애들의 조합을 보기 위해 n*n*2만큼의 시간이 든다.
따라서 두 개씩 합친 애들을 확인할 때는 완탐이 아니라 투포인터를 써보면 되겟다.
투포인터를 쓰면 n*n으로 해결 가능하다.
"""

t = int(stdin.readline())
for _ in range(t):
    k, n = map(int, stdin.readline().split())
    class1 = list(map(int, stdin.readline().split()))
    class2 = list(map(int, stdin.readline().split()))
    class3 = list(map(int, stdin.readline().split()))
    class4 = list(map(int, stdin.readline().split()))

    cand1 = []
    cand2 = []

    for i in range(n):
        for j in range(n):
            cand1.append(class1[i] + class2[j])
    for i in range(n):
        for j in range(n):
            cand2.append(class3[i] + class4[j])

    cand1.sort()
    cand2.sort()

    start = 0
    end = len(cand1) - 1

    ans = []
    diff = 10**10
    while start < len(cand1) and end >= 0:
        cur_sum = cand1[start] + cand2[end]

        if abs(cur_sum - k) == diff:
            ans.append(cur_sum)
        elif abs(cur_sum - k) < diff:
            diff = abs(cur_sum - k)
            ans = []
            ans.append(cur_sum)

        if cur_sum > k:
            end -= 1
        elif cur_sum < k:
            start += 1
        else:
            break

    # diff == 0인 경우
    if start < len(cand1) and end >= 0:
        cur_sum = cand1[start] + cand2[end]

        if abs(cur_sum - k) < diff:
            ans.append(cur_sum)

    ans.sort()
    print(ans[0])
