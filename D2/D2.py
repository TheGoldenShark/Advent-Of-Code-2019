with open("input.txt","r") as f: data=f.readline()
data=data[:-1]
data=data.split(',')
data = [int(x) for x in data]
pointer=0
data[1]=12
data[2]=2
while pointer+3<len(data):
    if data[pointer]==1:
        data[data[pointer+3]] = data[data[pointer+1]]+data[data[pointer+2]]
        pointer+=4
    elif data[pointer]==2:
        data[data[pointer+3]] = data[data[pointer+1]]*data[data[pointer+2]]
        pointer+=4
    else:
        break
print(data[0])