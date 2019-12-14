# with open ("test1.txt","r") as f: data=f.readlines()
# with open ("test2.txt","r") as f: data=f.readlines()
with open("input.txt","r") as f: data=f.readlines()
data = ["".join(list(filter(lambda ch: ch not in ",", x)))[:-1].split(" ") for x in data]
data = [[tuple(x[:x.index("=>")]),tuple(x[x.index("=>")+1:])] for x in data]
recipeDict, leftOvers=dict(), dict()
for i in data:
    recipeDict[i[1][1]] = tuple([i[0],i[1][0]])
print("test")
for i in data:
    leftOvers[i[1][1]]=0
leftOvers["ORE"]=0
oreCount=0
def findOreCost(recipeDict, item, amount, oreCount, leftOvers):
    current=0
    current+=leftOvers[item]
    leftOvers[item]=0
    while current<int(amount):
        if item!="ORE":
            for i in range(0,len(recipeDict[item][0]), 2):
                oreCount = findOreCost(recipeDict, recipeDict[item][0][i+1], recipeDict[item][0][i], oreCount, leftOvers)
            current += int(recipeDict[item][1])
        else:
            oreCount+=1
            current+=1
    if current>int(amount):
        current-=int(amount)
        leftOvers[item] += current
    return oreCount

finalOreCount=0
fuel=0
while finalOreCount<1000000000000:
    finalOreCount += findOreCost(recipeDict,"FUEL",1,oreCount,leftOvers)
    fuel+=1
    print(finalOreCount)
print("FUEL")
print(fuel)