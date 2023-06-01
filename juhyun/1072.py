import sys,math
input = sys.stdin.readline

X,Y = map(int,input().split())

def now_z(x,y):
    return int(y*100/x)

lt = 0
rt = X

now_Z = now_z(X,Y)

while lt <= rt:
    mid = int((lt + rt)/2)

    new_Z = now_z(X + mid , Y + mid)

    if new_Z > now_Z:
        rt = mid -1
    else:
        lt = mid + 1
    
print(lt if lt <= X else -1)