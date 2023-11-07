N = int(input())

X = list(map(int, input().split()))
Y = list(map(int, input().split()))

flow = [0 for _ in range(N)]
diff = [0 for _ in range(N)]
for i in range(N):
    if X[i] > Y[i]:
        flow[i] = -1
    elif X[i] < Y[i]:
        flow[i] = 1
    
    diff[i] = abs(X[i] - Y[i])


current_direction = flow[0]
st, en = 0, -1
ans = 0
print
for i in range(N):

    
    if flow[i] != current_direction or flow[i] == 0:
        en = i-1
        # print(st, en)

        di = diff[st:en+1]
        if len(di) != 0:
            ans += max(diff[st:en+1])

        current_direction = flow[i]
        st = i

ans += max(diff[st:N+1])


print(ans)


'''
4
2 2 2 2
2 2 2 2


5
1 1 1 1 1
5 3 1 3 5
'''