
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
        for elemento in self.items: print(elemento, end="")
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
    special_case = True
    deque_scramble = deque()     #deque result
    store_stacks = []    #list to store stacks, sorted by appearance [flow controlled by '(' and ')']
    stack_scramble = Stack()    #stack to put char that appeared between parenteses
    for char in array:
        if(char == '('):
            flux = True
            if not stack_scramble.isEmpty(): store_stacks.append(stack_scramble)
            stack_scramble = Stack()
        elif(char == ')'):
            special_case = False
            flux = False
            if not stack_scramble.isEmpty(): store_stacks.append(stack_scramble)
            for stack in store_stacks:
                while(not stack.isEmpty()):
                    deque_scramble.appendleft(stack.pop())
        else:
            if(flux):
                stack_scramble.push(char)
            else:                
                deque_scramble.append(char)

    #if open some '(' and never close it    
    if(special_case):
        for i in range(len(store_stacks)):
            stack = store_stacks[i]
            if(not stack.isEmpty()):
                while(not stack.isEmpty()):
                    deque_scramble.appendleft(stack.pop())

    # avoid desapearement of some chars stored in the stack_scramble
    if(not stack_scramble.isEmpty()):
        while(not stack_scramble.isEmpty()):
            deque_scramble.appendleft(stack_scramble.pop())


    if(len(deque_scramble) != 0):
        while(len(deque_scramble) != 0):
            print(deque_scramble.popleft(), end="")
        print()


def dekey(request):
    times = int(request[0])
    address = deque()

    encrypted_address = request[1:]
    # encrypted_address = "".join(encrypted_address)

    #initializing deque_adrress
    for slot in encrypted_address:
        address.append(slot)

    #decrypting the address
    for i in range(times):
        a = address.popleft()
        b = address.popleft()

        if(int(a) > int(b)):
            address.appendleft(a)
            address.append(b)
        else:
            address.appendleft(b)
            address.append(a)
    
    for i in range(len(address)):
        print(address.popleft(), end="")
    print()

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
            #getting from dict the instruction to execute with the address
            char_array = [*dic_next_process.values()][0][1:]
            dekey(char_array)

    entrada = input().split()

print(f'{len(process)} processo(s) órfão(s).')
