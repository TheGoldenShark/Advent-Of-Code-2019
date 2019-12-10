with open("input.txt","r") as f: data=f.readline()[:-1]
n=25*6
layers = [data[i:i+n] for i in range(0,len(data),n)]
minLayer,minCount=list(),999999999999
for i in layers:
    temp = i.count("0")
    if temp<minCount:
        minLayer=i
        minCount=temp
print(minLayer.count("1")*minLayer.count("2"))