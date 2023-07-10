
def replaceStr(str) :
    i = 0
    if str.find('&') or str.find('(') or str.find(')') or str.find('.') or str.find(',') or str.find('-'):
        i = 1

    return (str.replace('&', '').replace('(', '').replace(')', '').replace('.', '').replace(',', '').replace('-', '').replace(' ', ''), i)

def solution(merchantNames):
    merchantNames.sort(reverse=True)
    for num, merchant in enumerate(merchantNames) :

        remove_arr = []
        re_merchant, m = replaceStr(merchant)

        for index in range(len(merchantNames)) :
            if num == index :
                continue
            real = merchantNames[index]
            index_, n = replaceStr(real)

            if re_merchant.find(index_) != -1 :
                if re_merchant == index_ and m > n :
                    remove_arr.append(merchant)
                else :
                    remove_arr.append(real)
        remove_arr = list(set(remove_arr))
        for i in remove_arr :
            merchantNames.remove(i)

    print(merchantNames)




# solution(["토스커피사일로 베이커리", "토스커피사일", "토스커피사일로 베이커", "토스커피사일로 베이", "토스커피사일로&베이커리"])
solution(["비바리퍼블리", "토스커피사일로 베이커리", "비바리퍼블리카 식당", "토스커피사일", "토스커피사일로 베이커", "비바리퍼블리카식", "토스커피사일로 베이", "토스커피사일로&베이커리"])

