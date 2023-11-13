import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = list(map(int, input().rstrip().split() ))

strings = []



for i in range(N):
    
    dic = {}
    dic2 = {}
    for i in range(97, 123):
        dic[chr(i)] = 0
        dic2[chr(i)] = 0

    string = input().rstrip()
    val = 0
    for char in string:
        if dic[char] == 0:
            val += 1
        dic[char] = 1
        dic2[char] = 1
        
        

    strings.append([dic, val, val, dic2])

# print(strings)
    

for j in range(M):
    o, x = list(input().rstrip().split())
    ans = 0
    if o == '1':
        for string in strings:
            if string[3][x] == 1 and string[0][x] == 1:
                string[0][x] = 0
                string[2] -= 1
            if string[1] == string[2]:
                ans += 1

            # print(string[1], string[2])
    else:
        for string in strings:
            if string[3][x] == 1 and string[0][x] == 0:
                string[0][x] = 1
                string[2] += 1
            if string[1] == string[2]:
                ans += 1

            # print(string[1], string[2])
    
    # print("\n\n")
    # print(str(ans))
    print(str(ans) + "\n")
        

