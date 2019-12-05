with open("input.txt","r") as f: data=f.readline()
#Test should return 1 or 0
# data = '3,9,8,9,10,9,4,9,99,-1,8 '
data = [int(x) for x in data[:-1].split(',')]
pointer=0
valI = [False, False, False]

def setVals(data,pointer,valI,noVals):
    val = []
    for i in range(0,noVals):
        if valI[i]:
            val.append(data[pointer+i+1])
        else:
            val.append(data[data[pointer+i+1]])
    return val
while True:
    iStuff = str(data[pointer])[:-2][::-1]
    for i in range(0,3):
        if len(iStuff)<=i:
            valI[i]=False
        else:
            valI[i]=bool(int(iStuff[i]))

    #Add
    if str(data[pointer])[-1]=="1":
        valI[2]=True
        val = setVals(data,pointer,valI,3)
        data[val[2]] = val[0]+val[1]
        pointer+=4
    #Multiply
    elif str(data[pointer])[-1]=="2":
        valI[2]=True
        val = setVals(data,pointer,valI,3)
        data[val[2]] = val[0]*val[1]
        pointer+=4
    #Input
    elif str(data[pointer])[-1]=="3":
        valI[0]=True
        val = setVals(data,pointer,valI,1)
        print("--- Input Number ---")
        val.append(int(input(">> ")))
        data[val[0]] = val[1]
        pointer+=2
    #Output
    elif str(data[pointer])[-1]=="4":
        val = setVals(data,pointer,valI,1)
        print(val[0])
        pointer+=2
    #jump-if-true
    elif str(data[pointer])[-1]=="5":
        val = setVals(data,pointer,valI,2)
        if val[0]!=0:
            pointer=val[1]
        else:
            pointer+=3
    #jump-if-false
    elif str(data[pointer])[-1]=="6":
        val = setVals(data,pointer,valI,2)
        if val[0]==0:
            pointer=val[1]
        else:
            pointer+=3
    #less-than
    elif str(data[pointer])[-1]=="7":
        valI[2]=True
        val = setVals(data,pointer,valI,3)
        if val[0] < val[1]:
            data[val[2]] = 1
        else:
            data[val[2]] = 0
        pointer+=4
    #equals
    elif str(data[pointer])[-1]=="8":
        valI[2]=True
        val = setVals(data,pointer,valI,3)
        if val[0] == val[1]:
            data[val[2]] = 1
        else:
            data[val[2]] = 0
        pointer+=4
    #Stop
    else: break

