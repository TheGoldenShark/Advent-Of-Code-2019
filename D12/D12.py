with open("input.txt","r") as f: data=f.readlines()
dataNew=[]
for x in data:
    dataNew.append(("").join(list(filter(lambda ch: ch not in "<>xyz= ", x))[:-1]).split(","))   
for x in range(0,len(dataNew)):
    for y in range(0,len(dataNew[x])):
        dataNew[x][y] = int(dataNew[x][y])
data=list(dataNew)

time=0
moons=[]
class moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]
for i in data:
    moons.append(moon(i))
for z in range(0,1000):
    for i in moons:
        for k in moons:
            if i.pos==k.pos:
                pass
            else:
                for j in range(0,3):
                    if i.pos[j]!=k.pos[j]:
                        i.vel[j]+=(k.pos[j]-i.pos[j])/abs((k.pos[j]-i.pos[j]))
    for k in moons:
        for i in range(0,3):
            k.pos[i]+=k.vel[i]

nrg=0
for f in moons:
    temp1=0
    temp2=0
    for i in range(0,3):
        temp1+=abs(f.vel[i])
        temp2+=abs(f.pos[i])
    nrg+=temp1*temp2

print(int(nrg))

