
arr_size =  100_010
N, K, S = list(map(int, input().split()))
arr = [0 for _ in range(arr_size)]


for i in range(N) :
    index, num = list(map(int, input().split()))
    arr[index] = num

answer = 0
bus = 0


for i in range(0, S) :
    distance = (S - i)
    if arr[i] != 0 :
        if bus + arr[i] >= K :
            q = 0
            if bus == 0 :
                q = arr[i] // K
                arr[i] -= (K - bus)
            else :
                arr[i] -= (K - bus)
                q = arr[i] // K
            
            
            if arr[i] % K != 0 :
                answer += ((q+1) * distance)*2
            else :
                answer += ((q) * distance)*2
            bus = arr[i] % K
        else :
            if bus != 0 :
                bus += arr[i]
            else : 
                answer += distance * 2
                bus += arr[i]
    


bus = 0
S = (arr_size - S)
arr = arr[-1:-S:-1]
S -= 1
for i in range(0, S) :
    distance = (S - i)
    if arr[i] != 0 :
        if bus + arr[i] >= K :
            q = 0
            if bus == 0 :
                q = arr[i] // K
                arr[i] -= (K - bus)
            else :
                arr[i] -= (K - bus)
                q = arr[i] // K
            
            
            if arr[i] % K != 0 :
                answer += ((q+1) * distance)*2
            else :
                answer += ((q) * distance)*2
            bus = arr[i] % K
        else :
            if bus != 0 :
                bus += arr[i]
            else : 
                answer += distance * 2
                bus += arr[i]


print(answer)


        