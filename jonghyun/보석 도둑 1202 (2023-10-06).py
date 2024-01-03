from heapq import heappush, heappop

N, K = list(map(int, input().split()))

bags = []
jewels = []
heap = []

for _ in range(N):
    Mi, Vi = list(map(int, input().split()))
    jewels.append((Vi, Mi))
    heappush(heap, (-1*Vi, Mi))

for _ in range(K):
    bags.append(int(input()))

bags.sort()


def binarySearch(arr, value):
    st = 0
    en = len(arr) - 1
    mid = 0
    while st <= en:
        mid = (st + en) // 2
        if value > arr[mid]:
            st = mid + 1
        elif value < arr[mid]:
            en = mid -1
        elif value == arr[mid]:
            return mid
    
    return st


bags.sort()

answer = 0
# print(bags)
# print(binarySearch(bags, 10000))
while heap:
    Vi, Mi = heappop(heap)
    Vi *= -1
    # print(f"Vi, Mi : {(Vi, Mi)}")
    index = binarySearch(bags, Mi)
    # print(f"index : {index}")
    if index >= len(bags) or index <= -1:
        continue
    del bags[index]
    answer += Vi

print(answer)