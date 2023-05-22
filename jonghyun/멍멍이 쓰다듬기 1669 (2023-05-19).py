def dfs():
    pass


def solution() :
    x, y = list(map(int, input().split()))

    answer = 1
    diff = y - x - 1
    print(2**31)
    check = [0 for _ in range(2**31)]
    dfs()

solution()