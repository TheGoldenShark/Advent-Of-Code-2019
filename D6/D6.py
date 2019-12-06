with open("input.txt","r") as f: data=f.readlines()
data = [x[:-1].split(")") for x in data]
def parent(planet, data):
    parentNo=0
    for sublist in data:
        if sublist[1] == planet:
           parentNo = parent(sublist[0],data)
           return parentNo+1
    return parentNo

total=0
for i in data:
    total+=parent(i[1],data)

print(total)    