n = int(input())

arr = list(map(int,input().split()))        # queue
stack = []                                  # stack

cnt = 1

while arr:
    if cnt == arr[0]: 
        cnt+=1
        arr.pop(0)
    else:
        stack.append(arr.pop(0))
        
    while stack:
        if stack[-1] == cnt:
            stack.pop()
            cnt += 1
        else:
            break

if len(stack) == 0:
    print("Nice")
else:
    print("Sad")
    