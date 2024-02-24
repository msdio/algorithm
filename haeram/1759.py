from sys import stdin

"""
모두 구했을 때, 모음 한 개와 자음 두 개가 있는지 확인
이건 모음이 1개 이상, n-2개 이하로 있는지 확인하면 됨

알파벳 순서니까 정렬해야 함!!

이외에는 그냥 중복없이 인덱스 구하는거랑 똑같음
"""

l, c = map(int, stdin.readline().split())
arr = stdin.readline().split()
arr.sort()

idx = [0 for i in range(l)]

vowels = ["a", "e", "i", "o", "u"]


def check_arr(arr):
    password = convert_to_values(arr)  # 모음이 1개 이상, n-2개 이하로 있는지 확인

    cnt = 0

    for a in password:
        if a in vowels:
            cnt += 1

    if cnt >= 1 and cnt <= l - 2:
        return True, password
    else:
        return False, ""


def convert_to_values(idx):
    ret = ""

    for i in idx:
        ret += arr[i]

    return ret


def recur(cur, start):
    if cur == l:
        chk, val = check_arr(idx)
        if chk:
            print(val)

        return

    for i in range(start, c):
        idx[cur] = i
        recur(cur + 1, i + 1)


recur(0, 0)
