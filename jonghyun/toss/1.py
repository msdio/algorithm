from itertools import permutations

def solution(s, N):
    temp = [str(i) for i in range(1, N+1)]
    ans = -1
    for i in permutations(temp) :

        k = ''.join(i)
        # print(k)
        if s.find(k) != -1 :
            ans = max(int(ans), int(k))

    print(ans)
    return ans

solution("1451232125", 2) #21
solution("313253123", 3) # 312