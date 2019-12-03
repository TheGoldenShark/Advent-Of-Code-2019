with open("input.txt","r") as f: data = [int(x) for x in f.readline()[:-1].split(',')]
for i in range(0,100):
    for j in range(0,100):
        pointer=0
        dataNew=list(data)
        dataNew[1], dataNew[2]=i, j
        while pointer+3<len(dataNew):
            if dataNew[pointer]==1:
                dataNew[dataNew[pointer+3]] = dataNew[dataNew[pointer+1]]+dataNew[dataNew[pointer+2]]
            elif dataNew[pointer]==2:
                dataNew[dataNew[pointer+3]] = dataNew[dataNew[pointer+1]]*dataNew[dataNew[pointer+2]]
            else:
                break
            pointer+=4
        if dataNew[0] ==19690720:
            print((100*i) + j)