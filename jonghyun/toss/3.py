class Node:
    next = {}

    def __init__(self):
        self.next = {}

    def insert(self, merchant, idx):

        for i in merchant :
            if i in ['&', '(', ')', '.', ',', '-'] :
                if '&' in self.next[i] or

            if i in self.next :
                self.next[i].insert(merchant[idx+1:], idx + 1)
            else :
                self.next[i] = Node()
                self.next[i].insert(merchant[idx + 1:], idx + 1)



            if flag == 0:
                print(data[0])

            self.next[i].insert(data[1:], 1)
            return

        if flag == 0:
            print(data[0])

        self.next[i].insert(data[1:], flag)


def solution(merchantNames):

    for merchant in merchantNames :
        for i in merchant :


solution(
["비바리퍼블리", "토스커피사일로 베이커리", "비바리퍼블리카 식당", "토스커피사일", "토스커피사일로 베이커", "비바리퍼블리카식", "토스커피사일로 베이", "토스커피사일로&베이커리"])