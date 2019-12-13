with open("input.txt","r") as f: data=f.readline() 
data = [int(x) for x in data[:-1].split(',')]
# Size of memory is kn where n is size of instruction
size=100
pointer=0
relativeBase=0
paramMode = [False, False, False]
data = data + [0]*(size-1)*len(data)
outputTemp=[]
outputCounter=0
coords=set()
tileDict=dict()

def setVals(data,pointer,paramMode,noVals):
    register = []
    for i in range(0,noVals):
        #Indirect
        if paramMode[i]=="0":
            register.append(data[data[pointer+i+1]])
        # Immediate
        elif paramMode[i]=="1":
            register.append(data[pointer+i+1])
        # Relative Base
        elif paramMode[i]=="2":
            register.append(data[data[pointer+i+1]+relativeBase])
        # Relative Base Immediate
        elif paramMode[i]=="3":
            register.append(data[pointer+i+1]+relativeBase)
    return register
while True:
    paramMode = list(str(data[pointer]).zfill(5)[:-2][::-1])
    instruction = str(data[pointer]).zfill(5)[-2:]
    if instruction=="01":
        if paramMode[2]=="0": paramMode[2]="1"
        if paramMode[2]=="2": paramMode[2]="3"
        register = setVals(data,pointer,paramMode,3)
        data[register[2]] = register[0]+register[1]
        pointer+=4
    #Multiply
    elif instruction=="02":
        if paramMode[2]=="0": paramMode[2]="1"
        if paramMode[2]=="2": paramMode[2]="3"
        register = setVals(data,pointer,paramMode,3)
        data[register[2]] = register[0]*register[1]
        pointer+=4
    #Input
    elif instruction=="03":
        if paramMode[0]=="0": paramMode[0]="1"
        if paramMode[0]=="2": paramMode[0]="3"
        register = setVals(data,pointer,paramMode,1)
        print("--- Input Number ---")
        register.append(int(input(">> ")))
        data[register[0]] = register[1]
        pointer+=2
    #Output
    elif instruction=="04":
        register = setVals(data,pointer,paramMode,1)
        # print(register[0])
        if outputCounter!=3:
            outputTemp.append(register[0])
            outputCounter+=1
        if outputCounter==3:
            outputCounter=0
            coords.add(tuple(outputTemp[:-1]))
            tileDict[tuple(outputTemp[:-1])]=outputTemp[2]
            outputTemp=[]
        pointer+=2
    #jump-if-true
    elif instruction=="05":
        register = setVals(data,pointer,paramMode,2)
        if register[0]!=0:
            pointer=register[1]
        else:
            pointer+=3
    #jump-if-false
    elif instruction=="06":
        register = setVals(data,pointer,paramMode,2)
        if register[0]==0:
            pointer=register[1]
        else:
            pointer+=3
    #less-than
    elif instruction=="07":
        if paramMode[2]=="0": paramMode[2]="1"
        if paramMode[2]=="2": paramMode[2]="3"
        register = setVals(data,pointer,paramMode,3)
        if register[0] < register[1]:
            data[register[2]] = 1
        else:
            data[register[2]] = 0
        pointer+=4
    #equals
    elif instruction=="08":
        if paramMode[2]=="0": paramMode[2]="1"
        if paramMode[2]=="2": paramMode[2]="3"
        register = setVals(data,pointer,paramMode,3)
        if register[0] == register[1]:
            data[register[2]] = 1
        else:
            data[register[2]] = 0
        pointer+=4
    #addToBase
    elif instruction=="09":
        register = setVals(data,pointer,paramMode,1)
        relativeBase += register[0]
        pointer+=2
        pass
    #Stop
    elif instruction=="99":
        break

wallCount=0
for i in coords:
    if tileDict[i]==2:
        wallCount+=1


print(wallCount)
print("strongandstable5")