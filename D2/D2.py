with open("input.txt","r") as f: data=f.readline()
data = [int(x) for x in data[:-1].split(',')]
pointer=0
data[1], data[2]=12, 2
while pointer+3<len(data):
    if data[pointer]==1:
        data[data[pointer+3]] = data[data[pointer+1]]+data[data[pointer+2]]
    elif data[pointer]==2:
        data[data[pointer+3]] = data[data[pointer+1]]*data[data[pointer+2]]
    else: break
    pointer+=4
print(data[0])