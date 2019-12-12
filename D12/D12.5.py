from math import gcd
with open("input.txt","r") as f: data=f.readlines()
# with open("test.txt","r") as f: data=f.readlines()
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

sets=[set(),set(),set()]
facFound=[False,False,False]
fac=[0,0,0]
count=0
for i in data:
    moons.append(moon(i))
while not (facFound[0] and facFound[1] and facFound[2]):
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


    for l in range(0,3):
        temp = list()
        for m in moons:
            temp.append(tuple([m.pos[l],m.vel[l]]))
        temp=tuple(temp)
        if temp not in sets[l]:
            sets[l].add(temp)
        elif not facFound[l]:
            fac[l]=count
            facFound[l]=True
            print(str(count))
    count+=1
temp=abs(fac[0]*fac[1]) // gcd(fac[0],fac[1])
answer=abs(temp*fac[2]) // gcd(temp,fac[2])
print(answer)