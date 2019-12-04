input=[146810,612564]
valid=[]

def check(arr):
    arr=str(arr)
    double = False
    for i in range(0,len(arr)-1):
        if arr[i+1]>arr[i]:
            pass
        elif arr[i+1]==arr[i]:
            double=True
        else:
            return False
    if double==True: 
        return True
    else:
        return False

for i in range(input[0],input[1]+1):
    if check(i)==True:
        valid.append(i)

print(len(valid))



