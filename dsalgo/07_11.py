def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear + 1) % SIZE == front):
        return True
    else:
        return False
    
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False
        
        
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        queue[front] = None
    return queue[(front + 1) % SIZE]


SIZE = int(input("큐 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":
    select=input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    
    while (select != "ㅌ" and select != "X" and select != "x"):
        
        if (select == "I" or select == "i" or select == "ㅑ"):
            data = input("입력할 데이터--> ")
            enQueue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif (select == "E" or select == "e" or select == "ㄷ"):
            data = deQueue()
            print("추출된 데이터--> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif (select == "V" or select == "v" or select == "ㅍ"):
            data = peek()
            print("확인된 데이터--> ", data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print("입력이 잘못됨")
            
        select=input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
        
    print("프로그램 종료")