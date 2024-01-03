from collections import deque

N = int(input())


dq = deque()
for _ in range(N):
    dq.append(input())

# print(dq)
string = ""

# print(dq)
while dq:
    if len(dq) == 1:
        string += dq.popleft()
        continue

    if dq[-1] < dq[0]:
        string += dq.pop()
    elif dq[-1] > dq[0]:
        string += dq.popleft()
    else:
        i = 1
        
        # print(f"len(dq) - 1 - i, i : {len(dq) - 1 - i, i}")
        # print(f"dq[len(dq) - 1 - i], dq[i] : {dq[len(dq) - 1 - i], dq[i]}")
        while (len(dq) - 1 - i > i) and dq[len(dq) - 1 - i] == dq[i]:
            i += 1
        
        # print(f"i: {i}")
        if dq[len(dq) - 1 - i] >= dq[i]:
            string += dq.popleft()
        else:
            string += dq.pop()
    
    # print(dq)

for index, i in enumerate(string):
    print(i, end="")
    if (index+1) %80 == 0:
        print()








'''
10
K
K
K
A
C
K
A
K
K
K
KKKACKKKA

9

'''


'''
81
K
K
K
A
C
K
A
K
K
K
K
K
K
A
C
K
A
K
K
K
K
K
K
A
C
K
A
K
K
K
K
K
K
A
C
K
A
K
K
K
K
K
K
A
C
K
A
K
K
K
K
K
K
A
C
K
A
K
K
K
K
K
K
A
C
K
A
K
K
K
K
K
A
C
K
A
K
K

'''