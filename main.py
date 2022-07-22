from collections import deque

# Pilha (topo: esquerda // bottom: direita)
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)
      
    def pop(self):
        return self.items.pop(0)
      
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        for elemento in self.items: print(elemento)
        return ""


def enqueue(process, request):
    unordered_priority = Stack()
    priority = int(request[0])

    if(len(process) == 0):
        dic = {priority: request[1:]}
        process.appendleft(dic)
    else:
        #checks if there's tasks less priority
        for i in range(len(process)):
            current = process.__getitem__(i)
            key_current = list(current.keys())[0]

            #pop on process till fit the priority deque sort
            if(int(key_current) > priority):
                unordered_priority.push(process.popleft())

        #add the request, then put back lower (old) priorities requests
        dic = {priority: request[1:]}
        process.appendleft(dic)
        while(not unordered_priority.isEmpty()):
            process.appendleft(unordered_priority.pop())

    return process


entrada = input().split()
process = deque()

times = int
while entrada[0] != "stop":

    if(entrada[0] == "enqueue"):
        times = int(entrada[1])
        for i in range(times):
            request = input().split()            
            process = enqueue(process, request)

    elif(entrada[0] == "go"):
        pass

    entrada = input().split()

print(process)
