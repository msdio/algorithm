'''
p[0] = 1
p[1] = 2
p[2] = 0

b[0] = a[2]
b[1] = a[0]
b[2] = a[1]

b[p[0]] = a[0]
b[p[1]] = a[1]
b[p[2]] = a[2]
'''


def solution() :
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    # print(a, b)
    check = [0] * len(a)
    p = [0] * len(a)

    for i in range(len(a)) :
        for j in range(len(b)) :
            if b[j] == a[i] and check[j] == 0 :
                check[j] = 1
                p[i] = j
                break
    for i in p :
        print(i, end=" ")

solution()