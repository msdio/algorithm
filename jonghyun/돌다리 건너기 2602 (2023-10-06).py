

target = list(input())



string1 = list(input())
string2 = list(input())


dp1 = [[0 for j in range(len(string1))] for i in range(len(target))]
dp2 = [[0 for j in range(len(string1))] for i in range(len(target))]


def dpSolve(dp1, dp2, i, target, string1):
    for i in range(len(target)):
        char = target[i]


        if i == 0 and char == string1[j]:
            dp1[0][j] = dp1[0][j-1] + 1
            continue
        elif i == 0 and char != string1[j]:
            dp1[0][j] = dp1[0][j-1]
            continue

        if j == 0:
            continue

        if char == string1[j]:
            dp1[i][j] = dp2[i-1][j-1] + dp1[i][j-1]
        else:
            dp1[i][j] = dp1[i][j-1]

for j in range(len(string1)):

    dpSolve(dp1, dp2, j, target, string1)
    dpSolve(dp2, dp1, j, target, string2)

print(dp1[-1][-1] + dp2[-1][-1])
# print("=== dp1 === ")
# print(*dp1, sep="\n")

# print("=== dp2 === ")
# print(*dp2, sep="\n")