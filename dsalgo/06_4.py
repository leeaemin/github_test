def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE - 1):
        return 1
    else:
        return 0
    

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print("stack is full")
        return
    top += 1
    stack[top] = data
    
SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", None]
top = 3

print(stack)
push("환타")
print(stack)
push("게토레이")