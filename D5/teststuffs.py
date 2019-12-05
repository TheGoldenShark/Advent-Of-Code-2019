data=10002
iStuff = str(data)[:-2]
iStuff = iStuff[::-1]
valI=[False,False,False]
for i in range(0,3):
    if len(iStuff)<=i:
        valI[i]=False
    else:
        valI[i]=bool(int(iStuff[i]))
print("test")
