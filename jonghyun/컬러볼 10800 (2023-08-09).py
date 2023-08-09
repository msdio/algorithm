from bisect import bisect_left

N = int(input())

histories = []
arr = [[] for _ in range(N + 1)]
all_arr = []

for i in range(N) :
    C, S = map(int, input().split())
    arr[C].append(S)
    all_arr.append(S)
    histories.append((C,S))

all_arr.sort()

accumulate_sum_arr = [[] for _ in range(N + 1)]
for index, temp_arr in enumerate(arr) :
    temp_arr.sort()
    change_arr = []
    accumulate_sum = 0
    for i in temp_arr :
        change_arr.append(accumulate_sum)
        accumulate_sum += i
        
    accumulate_sum_arr[index] = change_arr

accumulate_sum = 0
accumulate_sum_all_arr = []
for i in all_arr :
    accumulate_sum_all_arr.append(accumulate_sum)
    accumulate_sum += i

print(arr, all_arr)
print(accumulate_sum_arr, accumulate_sum_all_arr)

for history in histories :
    C, S = history
    index1 = bisect_left(all_arr, S)
    index2 = bisect_left(arr[C], S)
    
    print(accumulate_sum_all_arr[index1] - accumulate_sum_arr[C][index2])
