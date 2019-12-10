import math
with open("input.txt","r") as f: data=f.readlines()
# with open("test0.txt","r") as f: data=f.readlines()
coordAngle=dict()
data = [list(x[:-1]) for x in data]
maxView=0
for i in range(0,len(data)):
    for k in range(0,len(data[i])):
        if data[i][k]=="#":
            angleSet=set()
            for y in range(0,len(data)):
                for x in range(0,len(data)):
                    if data[y][x]=="#":
                        angleSet.add(round(math.atan2(y-i,x-k),4))
            if len(angleSet)>maxView: maxView=len(angleSet)
print(maxView)
        



