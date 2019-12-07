import itertools
phaseSettings = itertools.permutations([5,6,7,8,9])

with open("input.txt","r") as f: data=f.readline()


def setVals(memory,pointer,registerI,noVals):
    register = []
    for i in range(0,noVals):
        if registerI[i]:
            register.append(memory[pointer+i+1])
        else:
            register.append(memory[memory[pointer+i+1]])
    return register
def compute(phaseSetting, value, data):
    phaseDone=False
    memory = [int(x) for x in data[:-1].split(',')]
    pointer=0
    registerI = [False, False, False]
    while True:
        iStuff = str(memory[pointer])[:-2][::-1]
        for i in range(0,3):
            if len(iStuff)<=i:
                registerI[i]=False
            else:
                registerI[i]=bool(int(iStuff[i]))

        #Add
        if str(memory[pointer])[-1]=="1":
            registerI[2]=True
            register = setVals(memory,pointer,registerI,3)
            memory[register[2]] = register[0]+register[1]
            pointer+=4
        #Multiply
        elif str(memory[pointer])[-1]=="2":
            registerI[2]=True
            register = setVals(memory,pointer,registerI,3)
            memory[register[2]] = register[0]*register[1]
            pointer+=4
        #Input
        elif str(memory[pointer])[-1]=="3":
            registerI[0]=True
            register = setVals(memory,pointer,registerI,1)
            print("--- Input Number ---")
            if phaseDone==False:
                register.append(phaseSetting)
                phaseDone=True
            else:
                register.append(value)
            memory[register[0]] = register[1]
            pointer+=2
        #Output
        elif str(memory[pointer])[-1]=="4":
            register = setVals(memory,pointer,registerI,1)
            return(register[0])
            pointer+=2
        #jump-if-true
        elif str(memory[pointer])[-1]=="5":
            register = setVals(memory,pointer,registerI,2)
            if register[0]!=0:
                pointer=register[1]
            else:
                pointer+=3
        #jump-if-false
        elif str(memory[pointer])[-1]=="6":
            register = setVals(memory,pointer,registerI,2)
            if register[0]==0:
                pointer=register[1]
            else:
                pointer+=3
        #less-than
        elif str(memory[pointer])[-1]=="7":
            registerI[2]=True
            register = setVals(memory,pointer,registerI,3)
            if register[0] < register[1]:
                memory[register[2]] = 1
            else:
                memory[register[2]] = 0
            pointer+=4
        #equals
        elif str(memory[pointer])[-1]=="8":
            registerI[2]=True
            register = setVals(memory,pointer,registerI,3)
            if register[0] == register[1]:
                memory[register[2]] = 1
            else:
                memory[register[2]] = 0
            pointer+=4
        #Stop
        else: break

signal=[]
for i in phaseSettings:
    currentVal=0
    for k in i:
        currentVal = compute(k, currentVal, data)
        signal.append(currentVal)

print(max(signal))
    
