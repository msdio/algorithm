from bisect import bisect_left, bisect_right

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]


M, N, L = list(map(int, input().split()))
people = list(map(int, input().split()))
animals = []

for _ in range(N):
    x, y = list(map(int, input().split()))
    animals.append((x,y))



people.sort()
# print(people)
answer = 0
for animal in animals:
    x, y = animal
    if y > L:
        continue
    le = find_le(people, x)
    ri = find_ge(people, x)

    # print(f"x = {x}, le, ri : {le, ri}")

    if (le is not None and abs(x - le) + y <= L) or (ri is not None and abs(x - ri) + y <= L):
        answer += 1

print(answer)