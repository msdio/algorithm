k = 0
n = 0
people_target = []
people = []

def move(ladders, people) :
    people_temp = people[:]
    for index, person in enumerate(people) :
        if index == len(people) - 1 :
            if ladders[index - 1] == '-' :
                people_temp[index - 1] = person
            continue

        if index != 0 and ladders[index - 1] == '-':
            people_temp[index - 1] = person
            continue
        if ladders[index] == '-':
            people_temp[index + 1] = person
            continue
        people_temp[index] = person

    return people_temp


def main() :
    global k, n, people_target, people
    k = int(input())
    n = int(input())

    for i in range(k) :
        people.append(chr(i + ord('A')))

    people_target = list(input())

    is_question_mark = False
    ladders_arr = []
    for i in range(n) :
        ladders = list(input())
        if '?' in ladders :
            is_question_mark = True
            continue

        if is_question_mark :
            ladders_arr.append(ladders)
        else : 
            people = move(ladders, people)
    
    ladders_arr.reverse()
    for ladders in ladders_arr :
        people_target = move(ladders, people_target)

    answer = []
    index = 0

    # print(people, people_target, sep = "\n")

    for i in range(len(people)) :

        a = people_target[i-1] if i != 0 else None
        b = people_target[i] 

        c = None
        if i != len(people) - 1:
            c = people_target[i+1]

        # print(people[i] , (a, b, c))

        if people[i] not in (a, b, c) :
            for j in range(len(people) - 1) :
                print("x", end="")
            return
        

    while index < len(people) :
        if people[index] == people_target[index] :
            index += 1
            answer.append('*')
        else :
            answer.append('-')
            index += 2
            answer.append('*')
    
    print( ''.join(i for i in answer[0:len(answer) - 1]) )

main()

'''
3
3
CBA
-*
??
**


3
3
BCA
-*
??
**

11
5
CGBEDJFKIHA
*-***-****
-*-******-
??????????
-**-***-*-
**-*-*-*-*
'''