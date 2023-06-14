from itertools import permutations
import sys

input = sys.stdin.readline
# print = sys.stdout.write


def dfs(n, string) :
    global target, check, m
    if len(string) == len(target) :
        print("".join(string))
        # print(m)
        return
    else :
        for index, value in enumerate(target) :
            if check[index] == 1 :
                continue
            else :
                if ("".join(string) + value) in m:
                    continue
                else :
                    m["".join(string) + value] = 0

                check[index] = 1
                string.append(value)
                dfs(n+1, string)
                check[index] = 0
                string.pop()

for _ in range(int(input().rstrip())) :
    
    target = list(input().rstrip())
    target = sorted(target)
    check = [0 for _ in range(len(target))]
    m = {}
    dfs(0, [])