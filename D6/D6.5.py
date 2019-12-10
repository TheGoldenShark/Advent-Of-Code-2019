with open("input.txt","r") as f: data=f.readlines()
data = [x[:-1].split(")") for x in data]
sets=[set(),set()]
dists=[dict(),dict()]

def parent(planet, data, parentNo, i):
    global sets, dists
    for sublist in data:
        if sublist[1] == planet:
            parentNo+=1
            sets[i].add(tuple(sublist))
            dists[i][tuple(sublist)] = parentNo
            parent(sublist[0],data, parentNo, i)

parent("YOU",data, 0, 0)
parent("SAN",data, 0, 1)
results = sets[0].intersection(sets[1])
distances= [(dists[0][x] + dists[1][x]) for x in results]
print(min(distances)-4)   