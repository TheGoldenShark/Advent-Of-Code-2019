with open("input.txt","r") as f: data=f.readlines()
d = [int(x[:-1]) for x in d]
total=0
for i in data: total+=int(i/3)-2
print(total)