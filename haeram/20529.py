from sys import stdin

"""
MBTI를 숫자로 치환한다. 0 ~ 15까지.

그리고 윈도우를 움직이면서 세 숫자의 차이가 최소인 구간을 찾는다.
그리고 세 숫자를 통해 심리적인 거리를 계산한다.
"""

# t = int(stdin.readline())

# mbtis = {
#     "ISTJ": 0,
#     "ISFJ": 1,
#     "INFJ": 2,
#     "INTJ": 3,
#     "ISTP": 4,
#     "ISFP": 5,
#     "INFP": 6,
#     "INTP": 7,
#     "ESTP": 8,
#     "ESFP": 9,
#     "ENFP": 10,
#     "ENTP": 11,
#     "ESTJ": 12,
#     "ESFJ": 13,
#     "ENFJ": 14,
#     "ENTJ": 15,
# }


# def get_distance(n1, n2, n3):
#     return abs(n1 - n2) + abs(n2 - n3) + abs(n1 - n3)


# for _ in range(t):
#     n = int(stdin.readline())
#     arr = list(stdin.readline().split())

#     # convert mbtis into numbers
#     numbers = []
#     for a in arr:
#         numbers.append(mbtis[a])

#     numbers.sort()

#     # window
#     cur_min = 48  # 최대값은 16*3 = 48
#     ans = 48
#     for i in range(n - 2):
#         if numbers[i + 2] - numbers[i] < cur_min:
#             cur_min = numbers[i + 2] - numbers[i]
#             ans = get_distance(numbers[i], numbers[i + 1], numbers[i + 2])

#     print(ans)

##################################################################################

"""
아니.. 아예 잘못 생각했다.
"거리" 라는게 알파벳이 몇 개 다른지를 말하는 거였다... 아예 잘못 생각했네

그럼 윈도우 하면서 매번 거리를 계산하는 방법밖에 없겠다.
"""

# t = int(stdin.readline())


# def get_distance(s1, s2, s3):
#     cnt = 0
#     for i in range(4):
#         if s1[i] != s2[i]:
#             cnt += 1
#         if s2[i] != s3[i]:
#             cnt += 1
#         if s1[i] != s3[i]:
#             cnt += 1

#     return cnt


# for _ in range(t):
#     n = int(stdin.readline())
#     arr = list(stdin.readline().split())

#     arr.sort()

#     # window
#     ans = 12  # 거리의 최대값은 4*3 = 12
#     for i in range(n - 2):
#         cur = get_distance(arr[i], arr[i + 1], arr[i + 2])
#         ans = min(ans, cur)

#     print(ans)

##########################################################################

"""
이렇게 해도 안되는 이유
우선 알파벳 순으로 정렬한다고 해서 무조건 거리가 짧아지는게 아니다. 
완탐을 무조건 돌긴 해야 함
그러면 n^3 인데... 어떻게 시간을 줄일 수 있을까


"""

t = int(stdin.readline())


def get_distance(s1, s2, s3):
    cnt = 0
    for i in range(4):
        if s1[i] != s2[i]:
            cnt += 1
        if s2[i] != s3[i]:
            cnt += 1
        if s1[i] != s3[i]:
            cnt += 1

    return cnt


for _ in range(t):
    n = int(stdin.readline())
    arr = list(stdin.readline().split())

    if n > 16 * 2:
        print(0)
        continue

    ans = 48
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                ans = min(ans, get_distance(arr[i], arr[j], arr[k]))

    print(ans)
