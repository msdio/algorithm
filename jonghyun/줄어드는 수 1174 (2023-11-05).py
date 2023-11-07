
arr = ['0']
def recursive(max_depth, depth, num):
    global arr
    # print("depth, num : ", depth, num)
    if depth == max_depth:
        arr.append(num)
        return

    for i in range(10):
        if depth == 0 and i ==0 :
            continue
        
        if depth == 0:
            num += str(i)
        else:
            if int(num[depth-1]) <= i:
                break
            num += str(i)

        recursive(max_depth, depth+1, num)

        num = num[:-1]

for i in range(11):
    recursive(i, 0, '')

arr[1] = '0'

target = int(input())
if target >= len(arr):
    print(-1)
else:
    print(arr[target])


