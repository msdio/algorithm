from sys import stdin

"""
완탐으로 하려면 어떻게 할까?
1. 알파벳 종류 수를 구한다.
2. 종류 수 중에서 2개씩 뽑아가면서 최대 길이를 구한다.
3. 길이를 구할 때는 해당하는 애들을 1, 해당하지 않는 애들을 0으로 해놓고
1의 최대 길이를 구한다.

이건 26C2 * 10^6 이니까 될 리가 없다.

매 순간 몇 개의 문자를 몇 개씩 가지고 있는지 알고 있어야 한다.
딕셔너리 같은거 써볼까

문자의 개수를 세다가, 2개가 초과되는 순간 start 포인터를 증가시키면서
문자를 지우고 문자 개수가 2개 될 때까지 하나씩 지운다.
"""

n = int(stdin.readline())
lang = stdin.readline().rstrip()
len_lang = len(lang)

alp = {}

start = 0
end = 0
ans = 0
cur = 0
while end < len_lang:
    # 문자가 n개 이상이면, n개가 될 때까지 start를 앞으로 민다.
    if len(alp) > n:
        while len(alp) > n:
            alp[lang[start]] -= 1

            if alp[lang[start]] == 0:
                del alp[lang[start]]

            cur -= 1
            start += 1

    # 이미 있는 알파벳이라면 길이 증가
    if lang[end] in alp:
        alp[lang[end]] += 1
        cur += 1
    else:
        alp[lang[end]] = 1
        cur += 1

    end += 1
    if len(alp) <= n:
        ans = max(ans, cur)

print(ans)
