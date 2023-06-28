from collections import deque

N, M = list(map(int, input().split()))

li = list(map(int, input().split()))
true_people_num = li[0] 
true_people = li[1:]

graph = [[] for _ in range(N+1)]
people_list = []
for _ in range(M) :
    li = list(map(int, input().split()))
    people_num = li[0] 
    people = li[1:]
    people_list.append(people)
    for index, person in enumerate(people) :
        t = people[index]
        people_temp = people[:]
        people_temp.remove(person)
        # print(people_temp)
        graph[t].extend(people_temp)

for index, value in enumerate(graph) :
    graph[index] = list(set(value))

check = [0] * (N+1)
for true_person in true_people :
    check[true_person] = 1
    dq = deque()
    dq.append(true_person)
    while len(dq) != 0 :
        pop = dq.popleft()

        for i in graph[pop] :
            if check[i] == 1 :
                continue
            check[i] = 1
            dq.append(i)

ans = 0
for people in people_list :
    flag = False
    for person in people :
        if check[person] == 1 :
           flag = True

    if flag == False :
        ans += 1

print(ans)