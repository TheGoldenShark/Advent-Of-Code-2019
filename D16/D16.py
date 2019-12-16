with open("input.txt","r") as f: data=list(f.readline()[:-1])
# with open("test0.txt","r") as f: data=list(f.readline()[:-1])
# with open("test1.txt","r") as f: data=list(f.readline()[:-1])
basePattern = [0, 1, 0, -1]
# data=["1","2","3","4","5","6","7","8"]
def phase(data, basePattern):
    output=[]
    for i in range(0,len(data)):
        currentPattern=[]
        for j in basePattern:
            currentPattern.extend([j]*(i+1))
        currentPattern.append(currentPattern.pop(0))
        temp=0
        for j in range(0,len(data)):
            patternIndex=j%len(currentPattern)
            temp+=int(data[j]) * currentPattern[patternIndex]
        output.append(str(temp)[-1])
    return output

ans=list(data)
for i in range(0,100):
    ans = phase(ans, basePattern)

print("".join(ans)[:8])



