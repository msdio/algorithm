def bisect(x, y, plus, percent) :
    start = 0
    end = plus
    mid = (start + end) // 2
    while start <= end :
        mid = (start + end) // 2

        if (y + mid) *100  // (x + mid) <= percent :
            start = mid + 1
        else :
            answer = mid
            end = mid - 1
    return answer
        
                  


def init() :
    x, y= list(map(int, input().split()))
    
    if y == 0 :
        percent = 0
    else : 
        percent = (y * 100) // x


    if percent >= 99 :
        print(-1)
        return


    print( bisect(x, y, x, percent))        
init()