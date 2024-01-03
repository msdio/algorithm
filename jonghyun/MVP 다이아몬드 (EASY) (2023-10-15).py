N = int(input())
s, g, p, d = list(map(int, input().split()))
ranks = input()
answer = 0

before_val = 0

for rank in ranks:

    if rank == 'B':
        before_val = s - before_val - 1
        answer += before_val
    elif rank == 'S':
        before_val = g - before_val - 1
        answer += before_val
    elif rank == 'G':
        before_val = p - before_val - 1
        answer += before_val
    elif rank == 'P':
        before_val = d - before_val - 1
        answer += before_val
    elif rank == 'D':
        before_val = d
        answer += before_val

print(answer)