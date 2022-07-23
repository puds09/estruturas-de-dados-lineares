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
            current = process.__getitem__(0)
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

def scramble(array):
    # False = append on right || True = append on left
    flux = False 
    deque_scramble = deque()     #deque result
    store_stacks = []    #list to store stacks, sorted by appearance [flow controlled by '(' and ')']
    stack_scramble = Stack()    #stack to put char that appeared between parenteses
    for char in array:
        if(char == '('):
            flux = True
        elif(char == ')'):
            flux = False
        else:
            if(flux):
                stack_scramble.push(char)

            else:                
                deque_scramble.append(char)
                if(len(deque_scramble) != 0):
                    store_stacks.append(stack_scramble)
                    stack_scramble = Stack()

    for stack in store_stacks:
        while(not stack.isEmpty()):
            deque_scramble.appendleft(stack.pop())

    while(len(deque_scramble) != 0):
        print(deque_scramble.popleft(), end="")
    print()


# def dekey():

entrada = input().split()
process = deque()

times = int
while entrada[0] != "stop":

    if(entrada[0] == "enqueue"):
        times = int(entrada[1])
        for i in range(times):
            request = input().split()            
            process = enqueue(process, request)


    elif(entrada[0] == "go" and len(process) != 0):
        dic_next_process = process.pop()

        #getting the task to execute
        task = [*dic_next_process.values()][0][0]
        if(task == "scramble"):
            #getting from dict just the array of chars for unscramble
            char_array = [*dic_next_process.values()][0][1:][0]
            scramble(char_array)

        elif(task == "dekey"):
            pass

    entrada = input().split()

print(f'{len(process)} processo(s) órfão(s).')
