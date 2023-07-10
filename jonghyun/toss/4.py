from collections import deque



def f(li, before, after):
    if len(after) == 0:
        return
    action = after[0]
    if action in li:
        li.remove(action)
    before.appendleft(li[0])
    li.appendleft(action)
    global maxSize
    if len(li) > maxSize:
        li.pop()

def b(li, before, after):
    if len(before) == 0 :
        return
    action = before[0]
    if action in li:
        li.remove(action)
    after.appendleft(li[0])
    li.appendleft(action)
    global maxSize
    if len(li) > maxSize :
        li.pop()


def solution(maxSize1, actions):
    global maxSize
    maxSize = maxSize1
    li = deque()
    before = deque()
    after = deque()

    for action in actions :
        if action == 'B' :
            b(li, before, after)
        elif action == 'F' :
            f( li, before, after)
        else :
            direct(action, li, before, after)



    return list(li)



def direct(action,  li, before, after):

    if action in li:
        li.remove(action)
    if len(li) != 0:
        before.appendleft(li[0])
    after.clear()
    li.appendleft(action)


    global maxSize
    if len(li) > maxSize:
        li.pop()


# solution(3, ["1", "2", "3", "4", "3"])  # ["3", "4", "2"]
# solution(3, ["1", "2", "B", "B", "3"])  #["3", "1", "2"]
print( solution(
3, ["1", "3", "2", "B", "4", "F"]))