with open("input.txt","r") as f: data=f.readlines()
dataNew=[]
for x in data:
    dataNew.append(("").join(list(filter(lambda ch: ch not in "<>xyz= ", x))[:-1]).split(","))   
for x in range(0,len(dataNew)):
    for y in range(0,len(dataNew[x])):
        dataNew[x][y] = int(dataNew[x][y])
data=list(dataNew)

valsFound=[False,False,False]
time=0
moons=[]
class moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]
sets=[set(),set(),set()]
factors=[0,0,0]
for i in data:
    moons.append(moon(i))
count=1
while not (valsFound[0] and valsFound[1] and valsFound[2]):
    for i in moons:
        for k in moons:
            if i.pos==k.pos:
                pass
            else:
                for j in range(0,3):
                    if not valsFound[j]:
                        if tuple(i.pos[j]+i.vel[j]) not in sets[j]:
                            sets[j].add(tuple(i.pos[j]+i.vel[j]))
                        else:
                            factors[j] = count
                            valsFound[j] = True
    for k in moons:
        for i in range(0,3):
            k.pos[i]+=k.vel[i]
    count+=1
print("fini")

