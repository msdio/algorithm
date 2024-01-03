from bisect import bisect_left
import sys
# import gc


input = sys.stdin.readline
# print = sys.stdout.write


def getIndex(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

N, K, Q = list(map(int,input().split()))

for _ in range(Q):
    
    x, y = list(map(int,input().split()))
    
    if K == 1: 
        print(abs(x-y))
        continue

    
    y_list = [-y]
    
    while y >= 1:
        y = (y + K - 2) // K 
        y_list.append( -y )

    index = 0
    while x >= 1:
        
        tmp = getIndex(y_list, -x)
        # print("x, tmp:", x, tmp)
        if tmp != -1:
            print(index + tmp)
            # print("\n")
            break
            
        x = (x + K - 2) // K
        index += 1

'''
7 2 1
2 1
'''