with open("input.txt","r") as f: data=f.readline()
data = [int(x) for x in data[:-1].split(',')]
pointer=0
valI = [False, False, False]

def setVals(data,pointer,valI,noVals):
    val = [0,0,0]
    for i in range(0,noVals):
        if valI[i]:
            val[i]=data[pointer+i+1]
        else:
            val[i]=data[data[pointer+i+1]]
    return val

while pointer+3<len(data):
    iStuff = str(data[pointer])[:-2]
    iStuff = iStuff[::-1]
    for i in range(0,3):
        if len(iStuff)<=i:
            valI[i]=False
        else:
            valI[i]=bool(int(iStuff[i]))
    if str(data[pointer])[-1]=="1":
        valI[2]=True
        val = setVals(data,pointer,valI,3)
        data[val[2]] = val[0]+val[1]
        pointer+=4
    elif str(data[pointer])[-1]=="2":
        valI[2]=True
        val = setVals(data,pointer,valI,3)
        data[val[2]] = val[0]*val[1]
        pointer+=4
    elif str(data[pointer])[-1]=="3":
        valI[0]=True
        val = setVals(data,pointer,valI,1)
        print("--- Input Number ---")
        val[1] = int(input(">> "))
        data[val[0]] = val[1]
        pointer+=2
    elif str(data[pointer])[-1]=="4":
        valI[0]=True
        val = setVals(data,pointer,valI,1)
        print(data[val[0]])
        pointer+=2
    else: break

