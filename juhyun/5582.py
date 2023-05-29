import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()


board = [[0]*len(A) for _ in range(len(B))]

maxval = 0

for b in range(len(B)):
    for a in range(len(A)):
        # 처음이면 그냥 1
        if a == 0 or b == 0:
            if A[a] == B[b]:
                board[b][a] = 1
        else:
            if A[a] == B[b]:
                board[b][a] = board[b-1][a-1] + 1
        maxval = max(maxval, board[b][a])
print(maxval)
