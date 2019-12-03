with open("input.txt","r") as f: d=f.readlines()
d = [int(x[:-1]) for x in d]
total=0
for i in d: 
    i=(int(i/3))-2
    while i>0:
        total+=i
        i=(int(i/3))-2
print(total)