import sys
input = sys.stdin.readline
print = sys.stdout.write


class Node :
    next = []
    end = 0
    def __init__(self) :
        self.next = [0 for i in range(ord('a'), ord('z') + 1)]
        self.end = 0

    def insert(self, data, flag) :
        if data[0] == '\n' :
            self.end += 1
            if flag == 0 and self.end != 1:
                print(str(self.end))
            return

        i = ord(data[0]) - ord('a')
        
        if self.next[i] == 0 :
            self.next[i] = Node()
            
            if flag == 0 :
                print(data[0])

            self.next[i].insert(data[1:], 1)
            return
        
        if flag == 0 :
            print(data[0])

        self.next[i].insert(data[1:], flag)
        




n = int(input())
headNode = Node()
for _ in range(n):
    present_str = input()
    
    headNode.insert(present_str, 0)
    print("\n")