input=[146810,612564]
valid=[]

def check(arr):
    arr=str(arr)
    double = False
    for i in range(0,len(arr)-1):
        notHere=False
        if arr[i+1]>arr[i]:
            pass
        elif arr[i+1]==arr[i]:
            if i>0:
                if arr[i-1]==arr[i]:
                    notHere=True
            if i+2<=len(arr)-1:
                if arr[i+2]==arr[i]:
                    notHere=True
            if notHere==False:
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

# print(check(112233))
# print(check(123444))
# print(check(111122))


