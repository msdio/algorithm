from bisect import bisect_left, bisect_right

N= int(input())
A = list(map(int, input().split()))
dp = []
A_index = []
for i in range(len(A)):
    Ai = A[i]
    if len(dp) == 0:
        dp.append(Ai)
        A_index.append(0)
        continue
    
    if dp[-1] < Ai:
        dp.append(Ai)
        A_index.append(len(dp) -1)
    else:
        index = bisect_left(dp, Ai)
        dp[index] = Ai
        A_index.append(index)

max_size = len(dp)
print(max_size)
max_size -=1
answer_arr = []
for i in range(len(A_index)-1, -1, -1):
    if A_index[i] == max_size:
        answer_arr.append(A[i])
        max_size -= 1

for i in range(len(answer_arr)-1, -1, -1):
    print(answer_arr[i], end = " ")