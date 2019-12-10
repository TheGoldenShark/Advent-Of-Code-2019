import math
from operator import itemgetter
with open("input.txt","r") as f: data=f.readlines()
# with open("test3.txt","r") as f: data=f.readlines()
data = [list(x[:-1]) for x in data]
maxView=0
i=25
k=37
numAsteroids=200
# i=3
# k=8
# numAsteroids=9
angleSet=set()
angleList=list()
for y in range(0,len(data)):
    for x in range(0,len(data[y])):
        if data[y][x]=="#":
            angleList.append([math.atan2(y-i,x-k),[y,x]])
for i in range(0,len(angleList)):
    angleList[i][0]-=math.pi/2
    if angleList[i][0]<-1*math.pi:
        angleList[i][0]+=2*math.pi        
    angleList[i].append(angleList[i][1][0]**2 + angleList[i][1][1]**2)
for x in range(0,len(angleList)): angleList[x][0] = round(angleList[x][0],4)
angleList = sorted(angleList, key=itemgetter(0,2))
finalList=[]
# Sort into lists, pop from top one after the other, take 200th
lastPos=0
newPos=0
while True:
    newPos+=1
    if newPos<len(angleList):
        if angleList[newPos][0]!=angleList[lastPos][0]:
            finalList.append(angleList[lastPos:newPos])
            lastPos=newPos
    else:
        break
counter=1
i=0
while True:
    if len(finalList[i])>0:
        if counter!=numAsteroids:
            finalList[i].pop()  
            counter+=1                      
        else:
            output = finalList[i].pop()[1]  
            break
    i+=1
print(output[1]*100+output[0])