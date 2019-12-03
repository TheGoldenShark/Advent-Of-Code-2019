with open("input.txt","r") as f: data=f.readlines()
data=[i[:-1].split(",") for i in data]
dataNew=[]
for i in data:
    dataNew.append([[x[:1],int(x[1:])] for x in i])
visitedCoords = [set(),set()]
for i in range(0,len(dataNew)):
    currentPos=[0,0]
    distTravelled=0
    for j in dataNew[i]:
        for k in range(1,j[1]+1):
            if j[0] == "U": currentPos[1]+=1
            elif j[0] == "D": currentPos[1]-=1
            elif j[0] == "L": currentPos[0]-=1
            elif j[0] == "R": currentPos[0]+=1
            distTravelled+=1
            visitedCoords[i].add(tuple(currentPos))
results = visitedCoords[0].intersection(visitedCoords[1])
distances = [abs(x[0]) + abs(x[1]) for x in results]
mhDist = min(distances)
print(mhDist)