dic = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
    0: 6
}

def dfs(n, string):
    global dp

    if n < 0:
        dp[string] = 0
        return
    if n == 0:
        dp[string] = 2
        return

    for index, value in dic.items():
        string = string + str(index)
        if ''.join(sorted(string)) in dp:
            string = string[:-1]
            continue
        dp[''.join(sorted(string))] = 1
        dfs(n - value, ''.join(sorted(string)))
        string = string[:-1]



n = int(input())
for i in range(n):
    k = int(input())
    dp = {}
    dfs(k, '')
    
    # print(dp)
    min_v = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    max_v = -1
    for key, value in dp.items():
        if value == 2:
            max_v = max(int(''.join(sorted(key, reverse=True))), max_v)

            if key[0] == '0':
                m = 20
                swap_index = -1
                for index, i in enumerate(key):
                    if m >= int(i) and int(i) !=0:
                        m = int(i)
                        swap_index = index
                if swap_index != -1:
                    key = key[swap_index] + key[:swap_index] + key[swap_index+1:]
                else:
                    continue

            min_v = min(int(key), min_v)

    print(min_v, max_v)

