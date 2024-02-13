from sys import stdin

"""
그냥 완탐밖에 방법이 없을 것 같은데...?

1부터 가장 높은 나무통의 길이만큼 완탐을 돌리는 것 밖에 방법이 없을 것 같다.
나무통 높이 10000 * 한번에 나무들 다 확인하니까 10000 
시간 안에 될 것 같다.
"""

n, c, w = map(int, stdin.readline().split())
trees = [int(stdin.readline()) for _ in range(n)]

max_height = max(trees)


def tree_sold(height, tree_price, cutting_fee):
    revenue = 0

    for tree in trees:
        sold = 0
        cut = 0

        if tree % height == 0:
            cut = (tree // height) - 1
        else:
            cut = tree // height

        sold = tree // height

        cur = sold * height * tree_price - cut * cutting_fee

        if cur >= 0:
            revenue += cur

    return revenue


ans = 0
for i in range(1, max_height + 1):
    ans = max(ans, tree_sold(i, w, c))

print(ans)
